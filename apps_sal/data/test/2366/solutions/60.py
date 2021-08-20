from collections import Counter
N = int(input())
A = [int(x) for x in input().split()]
c = Counter(A)
ans = 0
for i in c:
    ans += c[i] * (c[i] - 1) // 2
for i in range(len(A)):
    if c[A[i]] == 1:
        print(ans)
    else:
        tmp = c[A[i]]
        print(ans - tmp * (tmp - 1) // 2 + (tmp - 1) * (tmp - 2) // 2)
