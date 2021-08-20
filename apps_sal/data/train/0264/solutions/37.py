class Solution:

    def maxLength(self, arr: List[str]) -> int:
        self.output = []
        self.res = 0
        self.dfs(arr)
        return self.res

    def checkUnique(self, s):
        m = set()
        for i in s:
            if i not in m:
                m.add(i)
            else:
                return False
        return True

    def dfs(self, arr, first=0, curr=[]):
        st = ''.join(curr)
        if self.checkUnique(st):
            self.output.append(st)
            self.res = max(len(st), self.res)
        for i in range(first, len(arr)):
            curr.append(arr[i])
            self.dfs(arr, i + 1, curr)
            curr.pop()
