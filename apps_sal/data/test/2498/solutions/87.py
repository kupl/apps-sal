from collections import deque, defaultdict


def gcd(a, b):
    return b if not a % b else gcd(b, a % b)


def lcm(a, b):
    return a * b // gcd(a, b)


(n, m) = list(map(int, input().split()))
A = [int(i) for i in input().split()]
tmp = A[0]
for i in range(1, n):
    tmp = lcm(tmp, A[i])
ans = m // tmp
lis = set()
for i in A:
    r = i
    k = 0
    while r % 2 == 0:
        k += 1
        r //= 2
    lis.add(k)
if m // tmp * tmp + tmp // 2 <= m:
    ans += 1
if len(lis) != 1:
    ans = 0
print(ans)
