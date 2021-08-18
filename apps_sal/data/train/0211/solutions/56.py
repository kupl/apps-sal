def partition(s):
    def backtrack(index, path):
        if index == len(s):
            res.append(list(path))
        else:
            path.append(s[index])
            backtrack(index + 1, path)
            path.pop()

            if path:
                path[-1] = path[-1] + s[index]
                backtrack(index + 1, path)
    res = []
    backtrack(0, [])
    return res


class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        ans = 0
        lst = partition(s)
        for prt in lst:
            if(len(set(prt)) == len(prt)):
                ans = max(ans, len(prt))
        return ans
