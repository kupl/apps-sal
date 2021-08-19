N = int(input())
A = list(map(int, input().split()))
r = 0
xor = 0
total = 0
cnt = 0
for l in range(N):
    while r < N and total + A[r] == xor ^ A[r]:
        total += A[r]
        xor ^= A[r]
        r += 1
    cnt += r - l
    total -= A[l]
    xor ^= A[l]
print(cnt)
