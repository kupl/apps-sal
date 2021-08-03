class Solution:
    def lastSubstring(self, s: str) -> str:
        if len({l for l in s}) == 1:
            return s
        arr = self.sort_bucket(s, (i for i in range(len(s))), 1)
        return s[arr[-1]:]

    def sort_bucket(self, s, bucket, order):
        d = defaultdict(list)
        for i in bucket:
            key = s[i:i + order]
            d[key].append(i)
        result = []
        for k, v in sorted(d.items()):
            if len(v) > 1:
                result += self.sort_bucket(s, v, order * 2)
            else:
                result.append(v[0])
        return result
