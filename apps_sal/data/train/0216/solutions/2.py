class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croaks = {'c': [], 'r': [], 'o': [], 'a': []}
        maxfrogs = 0
        i_croak = 0
        nfrogs = 0
        for sound in croakOfFrogs:
            if sound == 'c':
                i_croak += 1
                croaks['c'].append(i_croak)
                nfrogs += 1
                maxfrogs = max(nfrogs, maxfrogs)
            elif sound == 'r':
                if croaks['c']:
                    croaks['r'].append(croaks['c'].pop())
                else:
                    return -1
            elif sound == 'o':
                if croaks['r']:
                    croaks['o'].append(croaks['r'].pop())
                else:
                    return -1
            elif sound == 'a':
                if croaks['o']:
                    croaks['a'].append(croaks['o'].pop())
                else:
                    return -1
            elif sound == 'k':
                if croaks['a']:
                    croaks['a'].pop()
                    nfrogs -= 1
                else:
                    return -1
            else:
                return -1

        for sound in croaks:
            if croaks[sound] != []:
                return -1

        return maxfrogs
