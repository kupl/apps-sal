class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:

        if len(croakOfFrogs) % 5 != 0:
            return -1

        dic = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        numsCount = [0] * 5

        max_val = numOfFrogs = 0

        for i in range(len(croakOfFrogs)):

            if croakOfFrogs[i] == 'c':
                numOfFrogs += 1
            if croakOfFrogs[i] == 'k':
                numOfFrogs -= 1

            max_val = max(numOfFrogs, max_val)
            numsCount[dic[croakOfFrogs[i]]] += 1

            for j in range(0, 4):
                if numsCount[j] < numsCount[j + 1]:
                    return -1

        return max_val
