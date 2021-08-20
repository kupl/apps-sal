from collections import Counter
N = int(input())
A = list(map(int, input().split()))
L = [a + i for (a, i) in enumerate(A, 1)]
R = [a - i for (a, i) in enumerate(A, 1)]
ans = 0
R_c = Counter(R)
for l in L:
    ans += R_c[l]
print(ans)
