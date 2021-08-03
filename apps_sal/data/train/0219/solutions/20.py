class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        L = [1 if i > 8 else -1 for i in hours]
        K = [1 if i > 8 else -1 for i in hours]
        mp = {}
        for i in range(0, len(hours)):
            if i > 0:
                s = L[i] = L[i] + L[i - 1]
            else:
                s = L[i]
            if s not in mp:
                mp[s] = {i: True}
            else:
                mp[s][i] = True

        # print(K)
        # print(L)
        result = 0
        for i, c in enumerate(L):
            if L[-1] > L[i]:
                result = max(result, len(K) - i - 1)
                # print(\"ss\", i, result)
            if 0 < L[i]:
                result = max(result, i + 1)
                # print(\"ddd\", i)

            if i > 0 and L[i - 1] + 1 in mp:
                s = mp[L[i - 1] + 1]
                #print(result, s, i)
                result = max(result, max(s) - i + 1)
                #result = max(result, i + 1 - min(s))
            if L[i] - 1 in mp:
                s = mp[L[i] - 1]
                #print(result, s, i)
                # result = max(result, max(s) - i + 1)
                result = max(result, i - min(s))
            #print(result, i)
        return result

    def longestWPI(self, hours: List[int]) -> int:
        mp = {}
        accu = 0
        result = 0
        for i, v in enumerate(hours):
            accu += 1 if v > 8 else -1
            # print(accu)
            if accu > 0:
                result = max(result, i + 1)
                print((result, i))
            if accu - 1 in mp:
                result = max(result, i - mp[accu - 1])
                print((result, i))
            if accu not in mp:
                mp[accu] = i
        return result
