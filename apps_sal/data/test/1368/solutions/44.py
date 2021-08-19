import math
(N, A, B) = list(map(int, input().split()))
v = list(map(int, input().split()))
v.sort()
AAA = sum(v[N - A:]) / A
print(AAA)
p = 0
for i in range(A, B + 1):
    ans = v[N - i:]
    if sum(ans) / i == AAA:
        rest = v[:N - i]
        m = ans.count(ans[0])
        n = rest.count(ans[0])
        C = math.factorial(n + m) // (math.factorial(m) * math.factorial(n))
        p += C
print(p)
