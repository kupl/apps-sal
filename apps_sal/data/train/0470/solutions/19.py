class Solution:
    def threeSumMulti(self, A, target: int) -> int:
        M = 1000000007
        record = {}
        for i in A:
            if(i in record.keys()):
                record[i] = record[i] + 1
            else:
                record[i] = 1

        k_list = list(record.keys())
        k_list.sort()
        n = len(k_list)
        res = 0
        for i in range(n):
            for j in range(i, n):
                residual = target - k_list[i] - k_list[j]
                if(residual < k_list[j]):
                    continue
                if(i == j):
                    if(record[k_list[i]] == 1):
                        continue
                    else:
                        if(residual in record.keys()):
                            if(residual == k_list[j]):
                                res = res + int(record[k_list[i]] * (record[k_list[i]] - 1) * (record[k_list[i]] - 2) / 6)
                                res = res % M
                            else:
                                multi = record[residual]
                                res = res + int(record[k_list[i]] * (record[k_list[i]] - 1) / 2 * multi)
                                res = res % M
                        else:
                            continue

                else:
                    if(residual in record.keys()):
                        if(residual == k_list[j]):
                            res = res + int(record[k_list[i]] * (record[k_list[j]]) * (record[k_list[j]] - 1) / 2)
                            res = res % M
                        else:
                            multi = record[residual]
                            res = res + int(record[k_list[i]] * record[k_list[j]] * multi)
                            res = res % M
                    else:
                        continue

        return res
