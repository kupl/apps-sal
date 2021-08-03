n, k = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0
g = A[-1]
h = A[0]
p = 0
i = 1
c = 0
l = 0
while h > g and i < n:
    if A[i] == A[p]:
        p += 1
        i += 1
        continue

    for j in range(A[p] - A[i]):
        c += p + 1
        l += 1
        if c > k:
            ans += 1
            h -= l - 1
            c = p + 1
            l = 0
            if h <= g:
                break

    p = i
    i += 1

if h > g:
    ans += 1

print(ans)
