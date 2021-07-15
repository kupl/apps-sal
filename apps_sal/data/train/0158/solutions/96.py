class Solution:
     def kSimilarity(self, A: str, B: str) -> int:
        def mk_similarities(s): # len(s) == len(B)
            for i, c in enumerate(B):
                if s[i] != c:
                    break
            
            res = []
            for j in range(i + 1, len(B)):
                if s[j] == B[i]:
                    ns = list(s)
                    ns[i], ns[j] = ns[j], ns[i]
                    res.append(''.join(ns))
            return res
        
        N = len(A)
        ws = [A]
        swaps = 0
        seen = {A}
        while ws:
            nws = []
            for _ in range(len(ws)):
                s = ws.pop(0)
                # print(s)
                if s == B:
                    return swaps
                similarities = mk_similarities(s)
                # print(similarities)
                for similarity in similarities:
                    if similarity not in seen:
                        nws.append(similarity)
                        seen.add(similarity)
            ws = nws
            swaps += 1
        return None

