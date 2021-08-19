class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        numBlue = 0
        status = [0] * len(light)

        for i in range(len(light)):

            idx = light[i] - 1
            if idx == 0 or status[idx - 1] == 2:
                status[idx] = 2
                numBlue += 1
                idx += 1
                while idx != len(light) and status[idx] == 1:
                    status[idx] = 2
                    numBlue += 1
                    idx += 1

            else:
                status[idx] = 1
            # print(status)
            # print(numBlue)
            # print(i + 1)
            if numBlue == i + 1:
                res += 1

        return res
