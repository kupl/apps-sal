n = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(n - 2):
    s = L[i:i + 3][1]
    A = sorted(L[i:i + 3])
    t = A[1]
    if s == t:
        cnt += 1
print(cnt)
