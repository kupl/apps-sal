from collections import Counter


class Solution:

    def back(self, arr, soln, solns):
        if not arr:
            solns.append([len(soln), soln])
            return solns
        for i in range(len(arr)):
            sa = set(arr[i])
            sb = set(soln)
            c = dict(Counter(arr[i]))
            if max(c.values()) == 1 and len(sb.intersection(sa)) == 0:
                solncopy = soln
                solncopy += arr[i]
                solns = self.back(arr[i + 1:], solncopy, solns)
        solns.append([len(soln), soln])
        return solns

    def maxLength(self, arr: List[str]) -> int:
        solns = []
        for i in range(len(arr)):
            soln = arr[i]
            c = dict(Counter(arr[i]))
            if max(c.values()) == 1:
                solns = self.back(arr[i + 1:], soln, solns)
        if not solns:
            return 0
        return max(solns, key=lambda x: x[0])[0]
