from collections import Counter
N = int(input())
A = list(map(int, input().strip().split()))
C = Counter(A)
K = set(A)
ans = 0
for i in K:
    ans += C[i] * (C[i] - 1) // 2

for i in A:
    print(ans - (C[i] - 1))  # nシグマk = n(n-1)/2 ......
