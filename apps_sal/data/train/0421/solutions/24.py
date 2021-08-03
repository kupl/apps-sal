class Solution:
    def lastSubstring(self, s: str) -> str:
        # Keep track of the candidates for the maximum substring
        # then compare the next characters of the current candidates
        # and update the candidates list in which all candidates are equally likely to be the maximum subtring
        # if the length of the candidates list is equal to 1, then the candidate is the maximum subtstring

        candidate_indices = list(range(len(s)))  # at the start, every substring is a candidate
        index_offset = 0  # will be used to compare the next characters of the candidates

        while len(candidate_indices) > 1:  # Loop until we have more than one candidate
            # Using Python List Comprehension to find the maximum of the next char of the candidate
            current_max = max([s[candidate + index_offset] for candidate in candidate_indices if candidate + index_offset < len(s)])

            new_candidates = []  # used to update the candidates list

            # Find the starting index of the current_max character, i.e., finding the new list of candidates
            for i, candidate in enumerate(candidate_indices):

                # if the last char of the previous candidate is the start of the current candidate,
                # merge them together as one candidate
                if i > 0 and candidate_indices[i - 1] + index_offset == candidate:
                    continue  # Do not need to add the current candidate as the previous is added

                if candidate + index_offset > len(s) - 1:  # we are out of bounds, need to break the loop
                    break

                if s[candidate + index_offset] == current_max:  # found the candidate which has the current_max
                    new_candidates.append(candidate)  # append the starting index of the current best candidate

            candidate_indices = new_candidates  # Update the candidates
            index_offset += 1  # Consider the next character

        # if we are here, it means we have only one candidate, which is the starting index of the maximum substring
        return s[candidate_indices[0]:]

        # TIME and SPACE Complexities: O(n), where n - the length of the string


#         # The Naive Solution
#         # Keep track of the maximum string in a separate variable
#         # Do this for every character at index `i`  in string `s` like the following: s[i:]
#         # The drawback: string comparison takes O(n) time, and we need to do for every string
#         # starting with character at index `i`. So the overall time complexity would be
#         # O(n^2) - which is not good.

#         max_substring = \"\" # max_substring means the last substring in lexicographical order

#         for i in range(len(s)): # iterate over every character in the string
#             max_substring = max(s[i:], max_substring) # update the maximum substring if the new subtring is greater

#         return max_substring # return the maxium substring
