class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # Group letters by occurence
        # Ex: \"aaabaaa\" -> [['a', 3], ['b', 1], ['a', 3]]
        groups = []
        for key, group in itertools.groupby(text):
            groups.append([key, len(list(group))])

        # We need a counter to check if we can extend by one letter
        # Ex: \"aaa\" in \"aaabba\" can be extended to \"aaaa\" because we have another \"a\" at the end.
        count = collections.Counter(text)

        for index in range(len(groups)):
            # Check if we can merge two groups.
            # Ex \"aaa\" and \"aa\" in aaabaa\" can be merged to \"aaaaa\"
            if index <= len(groups) - 3:  # Make sure to dont go out of bounds
                # The next groups's length must be 1 to be able to merge
                if groups[index + 1][1] == 1 and groups[index + 2][0] == groups[index][0]:
                    groups[index][1] += groups[index + 2][1]

            # Length will be extend by 1 if there are more letters in available, as explained above.
            if count[groups[index][0]] > groups[index][1]:
                groups[index][1] += 1

        # Return the maximum length that exists
        maxlength = 0
        for group in groups:
            if group[1] > maxlength:
                maxlength = group[1]
        return maxlength
