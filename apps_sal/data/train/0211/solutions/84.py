import itertools
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        positions = []
        for i in range(1,len(s)):
            positions.append(i)
        if(len(s) < 3):
            if(s[0] != s[1]):
                return 2
        maximally_split = 1
        for i in range(1,len(s)):
            separate_positions = list(itertools.combinations(positions,i))
            for separate_position in separate_positions:
                curr_position = 0
                curr_idx = 0
                substrings = []
                while(curr_idx < len(separate_position)):
                    substrings.append(s[curr_position:separate_position[curr_idx]])
                    curr_position = separate_position[curr_idx]
                    curr_idx += 1
                substrings.append(s[curr_position:])
                length_of_unique_list = len(set(substrings))
                if(length_of_unique_list == len(substrings)):
                    if(length_of_unique_list > maximally_split):
                        maximally_split = length_of_unique_list
        if(len(set(list(s))) > maximally_split):
            maximally_split = len(set(list(s)))
        return maximally_split
