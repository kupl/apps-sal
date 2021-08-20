class Solution:

    def largestNumber(self, cost: List[int], target: int) -> str:
        Memo = {}
        Min = min(cost)
        Memo[0] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        def dfs(remain):
            if remain in Memo:
                return Memo[remain]
            if remain < Min:
                Memo[remain] = [0, 0, 0, 0, 0, 0, 0, 0, 0, -10000000]
                return [0, 0, 0, 0, 0, 0, 0, 0, 0, -10000000]
            Max = [0, 0, 0, 0, 0, 0, 0, 0, 0, -10000000]
            flag = False
            for (i, c) in enumerate(cost):
                tmp = dfs(remain - c)
                if tmp[-1] != -10000000:
                    flag = True
                    newtmp = tmp[:i] + [tmp[i] + 1] + tmp[i + 1:-1] + [tmp[-1] + 1]
                    for j in range(9, -1, -1):
                        if newtmp[j] > Max[j]:
                            Max = newtmp
                            break
                        elif newtmp[j] == Max[j]:
                            continue
                        else:
                            break
            Memo[remain] = Max
            return Max
        r = dfs(target)
        if r[-1] == -10000000:
            return '0'
        else:
            rs = ''
            for k in range(8, -1, -1):
                rs += str(k + 1) * r[k]
        return rs
