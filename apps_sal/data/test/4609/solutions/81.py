N = int(input())
A = []
count = 1
ans = 0
for _ in range(N):
    A.append(int(input()))
A.sort()
for i in range(N - 1):
    if A[i] == A[i + 1]:
        count += 1
    else:
        if count % 2 == 1:
            ans += 1
        count = 1
else:
    if count % 2 == 1:
        ans += 1
    else:
        count = 1
print(ans)
