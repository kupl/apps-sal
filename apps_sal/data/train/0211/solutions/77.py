class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        combin_dict = {s[0]: [set(s[0])]}
        for (index, char) in enumerate(s[1:]):
            new_dict = {}
            for (last_str, sets) in combin_dict.items():
                for combin_set in sets:
                    if char not in new_dict:
                        new_dict[char] = []
                    single_new_set = combin_set | set(char)
                    if len(''.join(combin_set)) == index + 1:
                        new_dict[char].append(single_new_set)
                    new_last = last_str + char
                    if len(''.join(combin_set)) == index + 1:
                        new_set = combin_set.difference(set([last_str]))
                    else:
                        new_set = combin_set
                    new_set.add(new_last)
                    if new_last not in new_dict:
                        new_dict[new_last] = []
                    new_dict[new_last].append(new_set)
            combin_dict = new_dict
        res = 0
        for (key, value) in combin_dict.items():
            for value_set in value:
                if len(''.join(value_set)) == len(s):
                    res = max(res, len(value_set))
        return res
