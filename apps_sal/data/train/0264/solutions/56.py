def bo(i):
    return ord(i) - ord('a')


class Solution:

    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        freq = []
        ans = 0
        for i in range(n):
            s1 = set()
            for j in arr[i]:
                s1.add(bo(j))
            if len(s1) == len(arr[i]):
                freq.append(s1)
        n = len(freq)
        for i in range(1 << n):
            s = set()
            cnt = 0
            for j in range(n):
                if i & 1 << j:
                    for k in freq[j]:
                        s.add(k)
                    cnt += len(freq[j])
                    if cnt != len(s):
                        break
            if cnt == len(s):
                ans = max(ans, cnt)
            if ans == 26:
                break
        return ans
