class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        amax = max(A)
        plist = [2]
        for k in range(3, int(sqrt(amax)) + 2, 2):
            for p in plist:
                if p * p > k:
                    plist.append(k)
                    break
                if k % p == 0:
                    break
            else:
                plist.append(k)
        pset = set(plist)
        amax //= 2
        n = n1 = n2 = len(A)
        k = 0
        while k < n1:
            x = A[k]
            if x in pset:
                n1 -= 1
                n2 -= 1
                A[k] = A[n1]
                A[n2] = x
                continue
            if x < plist[-1]:
                k += 1
                continue
            prime = True
            for p in plist:
                if p * p > x:
                    break
                if x % p == 0:
                    prime = False
                    break
            if not prime:
                k += 1
            else:
                n1 -= 1
                A[k] = A[n1]
                if x <= amax:
                    n2 -= 1
                    A[n2] = x
        ans = 1
        left = n - n2 + n1
        while left > ans and n1 > 0:
            n1 -= 1
            x = A[n1]
            found = False
            k = 0
            while k < n1:
                y = A[k]
                p = math.gcd(x, y)
                if p > 1:
                    found = True
                    n1 -= 1
                    A[k] = A[n1]
                    while p > 1:
                        y //= p
                        p = math.gcd(y, p)
                    x *= y
                else:
                    k += 1
                if k == n1 and found:
                    found = False
                    k = 0
            k = n - 1
            while k >= n2:
                if x % A[k] == 0:
                    A[k] = A[n2]
                    n2 += 1
                else:
                    k -= 1
            k = n - n2 + n1
            ans = max(ans, left - k)
            left = k
        return ans
