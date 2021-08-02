N = int(input())
A = list(map(int, input().split()))
ans = 0
n = 0
for i in range(N):
    if A[i] % 2 == 0:
        n += 1
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            ans += 1
        else:
            ans = 0
if ans == n:
    print("APPROVED")
else:
    print("DENIED")
