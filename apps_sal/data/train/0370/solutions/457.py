isp = [True for i in range(100000)]
pr = []
for i in range(2, 100000):
    c = i
    if isp[i]:
        pr.append(i)
        while c < 100000 - i:
            c += i
            isp[c] = False


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def pcr(n):
            r = n ** 0.5
            ans = {n}
            for p in pr:
                if p > r:
                    if n > 1:
                        ans.add(n)
                    break
                if n % p == 0:
                    ans.add(p)
                    while n % p == 0:
                        n = n // p
                    r = n ** 0.5
            return ans

        def iscf(n1, n2):
            (nn1, nn2) = (max(n1, n2), min(n1, n2))
            while nn1 % nn2 != 0:
                n1 = nn1 - nn2
                n2 = nn2
                (nn1, nn2) = (max(n1, n2), min(n1, n2))
            n = min(nn1, nn2)
            return True if n > 1 else False
        prn = {a: pcr(a) for a in A}
        print(prn)
        while True:
            rms = set()
            ks = list(prn.keys())
            kn = len(ks)
            for (i, k) in enumerate(ks):
                if len(prn[k]) == 1:
                    rms.add(k)
                    continue
                for j in range(i + 1, kn):
                    if len(prn[ks[j]]) == 1:
                        rms.add(ks[j])
                        continue
                    if prn[k].intersection(prn[ks[j]]):
                        prn[k].update(prn[ks[j]])
                        rms.add(ks[j])
                if rms:
                    break
            for k in rms:
                del prn[k]
            if not rms:
                break
        aa = set(A)
        cdd = [len(v & aa) for v in prn.values()]
        return max(cdd)
