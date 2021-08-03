from collections import Counter, defaultdict


class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:

        A.sort()
        dic = defaultdict(list)
        count = Counter(A)
        B = list(count.keys()) * 3
        B.sort()

        seen = set()

        ans = 0

        for i in range(len(B)):
            dic[B[i]].append(i)

        for i in range(len(B) - 2):
            for j in range(i + 1, len(B) - 1):
                temp = target - B[i] - B[j]

                if temp in dic:
                    k = dic[temp][-1]

                    if k > j:
                        seen.add((B[i], B[j], B[k]))

        def comb(n, m):
            N = list(range(n - m + 1, n + 1))
            M = list(range(1, m + 1))

            nn = 1
            mm = 1
            for i in N:
                nn *= i

            for i in M:
                mm *= i

            return int(nn / mm)

        for t in seen:
            temp = 1
            c = Counter(t)
            print(t)
            for i in c:
                m = c[i]
                n = count[i]
                if m > n:
                    temp = 0
                    break
                temp *= comb(n, m)
            ans += temp

        return ans % (10**9 + 7)
