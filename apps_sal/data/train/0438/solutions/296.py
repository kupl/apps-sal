class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        dic = {}

        def count_cluster(y, x, cur_count):
            length = 0
            if y[x - 1] == 0:
                if x < n:
                    if y[x + 1] == 0:
                        y[x] = 1
                        dic[x] = x
                        if m == 1:
                            cur_count += 1
                    else:
                        oldr = y[x + 1]
                        y[x] = 1 + y[x + 1]
                        y[dic[x + 1]] = y[x]
                        dic[x] = dic[x + 1]
                        dic[dic[x + 1]] = x
                        if oldr == m - 1:
                            cur_count += 1
                        if oldr == m:
                            cur_count -= 1
                else:
                    y[x] = 1
                    dic[x] = x
                    if m == 1:
                        cur_count += 1
            else:
                if x < n:
                    if y[x + 1] == 0:
                        oldl = y[x - 1]
                        y[x] = y[x - 1] + 1
                        y[dic[x - 1]] = y[x]
                        dic[x] = dic[x - 1]
                        dic[dic[x - 1]] = x
                        if oldl == m - 1:
                            cur_count += 1
                        if oldl == m:
                            cur_count -= 1
                    else:
                        oldr = y[x + 1]
                        oldl = y[x - 1]
                        y[x] = y[x - 1] + 1 + y[x + 1]
                        temp = dic[x - 1]

                        y[dic[x - 1]] = y[x]
                        dic[dic[x - 1]] = dic[x + 1]

                        y[dic[x + 1]] = y[x]
                        dic[dic[x + 1]] = temp

                        if oldr == m:
                            cur_count -= 1
                        if oldl == m:
                            cur_count -= 1
                        if oldr + oldl == m - 1:
                            cur_count += 1
                else:
                    oldl = y[x - 1]
                    y[x] = y[x - 1] + 1
                    y[dic[x - 1]] = y[x]
                    dic[x] = dic[x - 1]
                    dic[dic[x - 1]] = x
                    if oldl == m - 1:
                        cur_count += 1
                    if oldl == m:
                        cur_count -= 1

            return cur_count
        n = len(arr)

        s = [0] * (n + 1)
        last = -1
        cur_count = 0
        for idx, x in enumerate(arr):
            cur_count = count_cluster(s, x, cur_count)
            if cur_count > 0:
                last = idx + 1
        print(last)
        return last
