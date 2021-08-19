class Solution:

    def check_source(self, start_idx, s, source):
        i = 0
        while i < len(source):
            if start_idx == len(s):
                return False
            if source[i] != s[start_idx]:
                return False
            start_idx += 1
            i += 1
        return True

    def findReplaceString(self, s: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = []
        i = 0
        while i < len(s):
            if i in indexes:
                idx = indexes.index(i)
                source = sources[idx]
                target = targets[idx]
                if self.check_source(i, s, source):
                    i += len(source)
                    res.append(target)
                    continue
            res.append(s[i])
            i += 1
        return ''.join(res)
