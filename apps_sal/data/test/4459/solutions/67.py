from collections import Counter
N = int(input())
C = Counter(map(int, input().split()))
ans = 0
for i in C:
    if C[i] > i:
        ans += C[i] - i
    elif C[i] < i:
        ans += C[i]
print(ans)
