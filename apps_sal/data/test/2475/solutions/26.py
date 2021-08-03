N = int(input())
S = list(map(int, input().split()))
L = 0
R = N - 1
ans = 0
for i in range(1, (N + 1) // 2):
    r = R
    l = L
    j = 1
    a = 0
    Closed = set()
    while True:
        l += i
        Closed.add(l)
        r -= i
        if r in Closed:
            break
        Closed.add(r)
        if r < i:
            break
        a += S[l] + S[r]
        ans = max(ans, a)
        j += 1
print(ans)
