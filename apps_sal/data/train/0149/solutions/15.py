class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        distinct = len(set(s))
        while len(s) >= k:
            new_s = ''
            (cur, count) = (s[0], 1)
            for i in range(1, len(s)):
                print(cur, count)
                if s[i] == cur:
                    count += 1
                else:
                    new_s += cur * (count % k)
                    (cur, count) = (s[i], 1)
            new_s += cur * (count % k)
            if s == new_s:
                break
            s = new_s
        return s
