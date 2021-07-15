n = int(input())
A = tuple(map(int, input().split()))
c = 0
s = 0
r = 0
for l in range(n):
    while r < n and A[r] ^ s == A[r] + s:
        s = A[r] + s
        r += 1

    c += r- l
    if l == r:
        r += 1
    s -= A[l]

print(c)
