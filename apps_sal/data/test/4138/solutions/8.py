def solve(k):
    s = 0
    cur = 0
    j = -1
    for i in range(1, 19):
        p = 9 * 10**(i - 1)
        q = cur * p + i * p * (p + 1) // 2
        if k < s + q:
            j = i
            break
        s += q
        cur += i * p
        if s > 10**18:
            break
    k -= s
    left = 0; right = 9 * 10**(j - 1) + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if cur * mid + mid * (mid + 1) // 2 * j <= k:
            left = mid
        else:
            right = mid
    k -= cur * left + left * (left + 1) // 2 * j
    i = 1
    while 1:
        p = 9 * 10**(i - 1)
        if k <= i * p:
            l = k // i
            v = 10**(i - 1) + l
            return str(v)[k % i]
        k -= i * p
        i += 1


q = int(input())
for i in range(q):
    print(solve(int(input()) - 1))
