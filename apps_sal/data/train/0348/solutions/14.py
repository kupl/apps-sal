class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        dps = [elem for elem in arr]  # dps[i] LCS starting at i
        dpe = [elem for elem in arr]  # dpe[i] LCS ending at i
        dpt = [elem for elem in arr]  # dpt[i] = dpe[i-1] + dps[i+1]
        for i in range(len(arr)):
            if i != 0:
                dpe[i] = max(dpe[i], dpe[i] + dpe[i - 1])
                ip = len(arr) - i - 1
                dps[ip] = max(dps[ip], dps[ip] + dps[ip + 1])
        for i in range(len(arr)):
            if i != 0 and i != len(arr) - 1:
                dpt[i] = dpe[i - 1] + dps[i + 1]
            elif i == 0:
                dpt[i] = dps[i + 1]
            else:
                dpt[i] = dpe[i - 1]
        # print(dps,dpe,dpt)
        return max(max(dpt), max(dpe), max(dps))
