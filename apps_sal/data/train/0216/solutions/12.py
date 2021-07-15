class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # print(len(croakOfFrogs))
        if len(croakOfFrogs) % 5 > 0:
            return -1
        pos = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}
        count = [0]*5
        res = 1
        for c in croakOfFrogs:
            count[pos[c]] += 1
            # print(count)
            if pos[c] > 0:
                if count[pos[c]] > count[pos[c]-1]:
                    return -1
            if pos[c] == 4:
                for i in range(5):
                    count[i] -= 1
            elif pos[c] == 0:
                res = max(res, count[0])
        for i in range(4):
            if count[i+1] != count[i]:
                return -1
        return res
