class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        DP

        dp(i, k) := minimal length for encoded string starting from 'i' with 'k' characters removed
        dp(i, k) = min(dp(i, k-1), dp(j, k))
        """

        def segment2Len(segment):
            if segment[1] <= 1:
                return segment[1]
            return len(str(segment[1])) + 1
        segments = []
        start = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                segments.append([s[i - 1], i - start, start])
                start = i
        segments.append([s[-1], len(s) - start, start])

        def minLength(pChar, pLen, i, k, mem):
            key = (pChar, pLen, i, k)
            if key in mem:
                return mem[key]
            if k == 0:
                mem[key] = sum(map(segment2Len, segments[i:])) + segment2Len([pChar, pLen])
                return mem[key]
            if i == len(segments):
                mem[key] = segment2Len([pChar, max(0, pLen - k)])
                return mem[key]
            lengths = []
            curLen = pLen + 2
            for j in range(min(pLen, k) + 1):
                newLen = segment2Len([pChar, pLen - j])
                if newLen < curLen:
                    lengths.append(newLen + minLength(segments[i][0], segments[i][1], i + 1, k - j, mem))
                    curLen = newLen
            for j in range(i, len(segments)):
                subStrLen = segments[j][2] - segments[i][2]
                if subStrLen <= k:
                    if segments[j][0] == pChar:
                        lengths.append(minLength(pChar, pLen + segments[j][1], j + 1, k - subStrLen, mem))
                else:
                    break
            mem[key] = min(lengths)
            return mem[key]
        mem = {}
        ans = minLength('', 0, 0, k, mem)
        return ans
