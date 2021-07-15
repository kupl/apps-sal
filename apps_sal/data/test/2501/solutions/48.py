from collections import defaultdict

N = int(input())
A = [int(_) for _ in input().split()]

F = defaultdict(int)
B = defaultdict(int)

for i, v in enumerate(A):
    F[i+v] += 1
    B[i-v] += 1

ans = 0
for i in F:
    ans += F[i] * B[i]
print(ans)

