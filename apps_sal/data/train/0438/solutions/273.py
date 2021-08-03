class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        temp = [0] * len(arr)
        rn = [[None, None] for i in range(len(arr))]
        fans = None
        ans = set()
        st = 0
        for ind in arr:
            st += 1
            i = ind - 1
            temp[i] = 1

            if i == len(arr) - 1:
                rn[i] = [i, i]
                if temp[i - 1] == 1:
                    if tuple(rn[i - 1]) in ans:
                        ans.remove(tuple(rn[i - 1]))
                    mn, mx = rn[i - 1]
                    rn[i] = [min(mn, rn[i][0]), max(mx, rn[i][1])]
                    rn[rn[i][0]] = rn[rn[i][1]] = rn[i]

            elif i == 0:
                rn[i] = [i, i]
                if temp[i + 1] == 1:
                    if tuple(rn[i + 1]) in ans:
                        ans.remove(tuple(rn[i + 1]))
                    mn, mx = rn[i + 1]
                    rn[i] = [min(mn, rn[i][0]), max(mx, rn[i][1])]
                    rn[rn[i][0]] = rn[rn[i][1]] = rn[i]

            else:
                rn[i] = [i, i]
                if temp[i - 1] == 1:
                    if tuple(rn[i - 1]) in ans:
                        ans.remove(tuple(rn[i - 1]))
                    mn, mx = rn[i - 1]
                    rn[i] = [min(mn, rn[i][0]), max(mx, rn[i][1])]
                    rn[rn[i][0]] = rn[rn[i][1]] = rn[i]

                if temp[i + 1] == 1:
                    if tuple(rn[i + 1]) in ans:
                        ans.remove(tuple(rn[i + 1]))
                    mn, mx = rn[i + 1]
                    rn[i] = [min(mn, rn[i][0]), max(mx, rn[i][1])]
                    rn[rn[i][0]] = rn[rn[i][1]] = rn[i]

            if rn[i][1] - rn[i][0] == m - 1:
                ans.add(tuple(rn[i]))
            if ans:
                fans = st
        if fans:
            return fans
        return -1
