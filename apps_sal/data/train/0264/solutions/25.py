class Solution:

    def maxLength(self, arr: List[str]) -> int:

        def dfs(arr, path, res):
            if self.checkUnique(path):
                res.append(path)
            for i in range(len(arr)):
                dfs(arr[i + 1:], path + arr[i], res)
        (concatenated_string, res) = ([], 0)
        dfs(arr, '', concatenated_string)
        for elem in concatenated_string:
            res = max(res, len(elem))
        return res

    def checkUnique(self, string):
        dic = dict()
        for ch in string:
            if ch not in dic:
                dic[ch] = 1
            else:
                return False
        return True
