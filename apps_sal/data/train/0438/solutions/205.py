class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        if n == m:
            return n

        def helper(rec, k):
            temp_rec = []
            for i, j in rec:
                if k < i or k > j:
                    if j - i + 1 > m:
                        temp_rec.append([i, j])
                    continue
                if k - i == m or j - k == m:
                    return True
                else:
                    if k - i > m:
                        temp_rec.append([i, k - 1])
                    if j - k > m:
                        temp_rec.append([k + 1, j])
#            print(temp_rec)
            return temp_rec

        rec = [(1, n)]
        for ind in range(n, 0, -1):
            rec = helper(rec, arr[ind - 1])
#            print(rec)
            if rec == True:
                return ind - 1
            elif not rec:
                return -1
