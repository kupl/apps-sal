class Solution:

    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croaks = {'c': [], 'r': [], 'o': [], 'a': []}
        nfrogs = 0
        icroak = 0
        curfrogs = 0
        for sound in croakOfFrogs:
            if sound == 'c':
                icroak += 1
                croaks['c'].append(icroak)
                curfrogs += 1
                nfrogs = max(curfrogs, nfrogs)
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
                    curfrogs -= 1
                else:
                    return -1
            else:
                return -1
        for sound in croaks:
            if croaks[sound] != []:
                return -1
        return nfrogs
