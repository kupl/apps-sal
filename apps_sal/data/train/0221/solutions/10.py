class Solution:
    def longestDupSubstring(self, S: str) -> str:
        # def RabinKarp(text, M, q):
        #     if M == 0: return True
        #     h, t, d = (1<<(8*M-8))%q, 0, 256
        #     dic = defaultdict(list)
        #     for i in range(M):
        #         t = (d * t + ord(text[i]))% q
        #     dic[t].append(i-M+1)
        #     for i in range(len(text) - M):
        #         t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
        #         for j in dic[t]:
        #             if text[i+1:i+M+1] == text[j:j+M]:
        #                 return (True, text[j:j+M])
        #         dic[t].append(i+1)
        #     return (False, \"\")

        def check(sz):
            seen = defaultdict(list)
            cur, base, MOD = 0, 256, (1 << 31) - 1
            h = (1 << (sz * 8)) % MOD
            for i in range(sz):
                cur *= base
                cur += ord(S[i])
                cur %= MOD
            seen[cur].append(0)
            for i in range(sz, len(S)):
                cur *= base
                cur += ord(S[i])
                cur -= ord(S[i - sz]) * h
                cur %= MOD
                for j in seen[cur]:
                    if S[j:j + sz] == S[i - sz + 1:i + 1]:
                        return True, S[i - sz + 1:i + 1]
                seen[cur].append(i - sz + 1)
            return False, ''

        lo, hi = 1, len(S)
        res = ''
        # MOD = (1<<31) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            flag, tmp = check(mid)
            # flag, tmp = RabinKarp(S, mid, q)
            if flag:
                lo = mid + 1
                res = tmp
                # print(mid,res)
            else:
                hi = mid - 1
        # print(lo,hi)
        return res


# class Solution:
#     def RabinKarp(self,text, M, q):
#         if M == 0: return True
#         h, t, d = (1<<(8*M-8))%q, 0, 256

#         dic = defaultdict(list)

#         for i in range(M):
#             t = (d * t + ord(text[i]))% q

#         dic[t].append(i-M+1)

#         for i in range(len(text) - M):
#             t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
#             for j in dic[t]:
#                 if text[i+1:i+M+1] == text[j:j+M]:
#                     return (True, text[j:j+M])
#             dic[t].append(i+1)
#         return (False, \"\")

#     def longestDupSubstring(self, S):
#         beg, end = 0, len(S)
#         q = (1<<31) - 1
#         Found = \"\"
#         while beg + 1 < end:
#             mid = (beg + end)//2
#             isFound, candidate = self.RabinKarp(S, mid, q)
#             if isFound:
#                 beg, Found = mid, candidate
#             else:
#                 end = mid

#         return Found
