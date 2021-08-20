class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        frog_counter = 0
        crk_dict = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        if croakOfFrogs[0] != 'c':
            return -1
        elif croakOfFrogs[-1] != 'k':
            return -1
        else:
            for i in range(len(croakOfFrogs)):
                if crk_dict['c'] >= crk_dict['r'] >= crk_dict['o'] >= crk_dict['a'] >= crk_dict['k']:
                    crk_dict[croakOfFrogs[i]] += 1
                    if frog_counter < crk_dict['c']:
                        frog_counter += 1
                    if croakOfFrogs[i] == 'k':
                        for m in crk_dict:
                            crk_dict[m] -= 1
                else:
                    return -1
            return frog_counter
