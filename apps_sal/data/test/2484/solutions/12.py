n = int(input())
A = list(map(int, input().split()))
ans = 0
l = 0
r = 0
bit = A[0]
total = A[0]
while True:
    if bit == total:
        ans += r - l + 1
        r += 1
        if r == n:
            break
        total += A[r]
        bit ^= A[r]
    else:
        total -= A[l]
        bit ^= A[l]
        l += 1
print(ans)
