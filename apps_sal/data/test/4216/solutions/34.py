N = int(input())
A = 1
ans = len(str(N))
while A ** 2 <= N:
    if N % A == 0:
        B = int(N / A)
        num = max(len(str(A)), len(str(B)))
        ans = min(ans, num)
    A += 1
print(ans)
