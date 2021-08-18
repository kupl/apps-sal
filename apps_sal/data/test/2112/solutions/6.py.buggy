(n, m) = map(int, input().split())
(x, k, y) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
j = 0
for i in range(n):
    if j >= m:
        break
    if a[i] == b[j]:
        c.append(0)
        j += 1
    else:
        c.append(1)

if j != m:
    print(-1)
    return

while len(c) != n:
    c.append(1)

back_l = -1
back_r = -1
ans = 0
while True:
    l = back_l
    r = back_r
    for i in range(back_r + 1, n):
        if c[i] == 1:
            l = i
            r = i
            break
    M = 0
    for i in range(r, n):
        M = max(M, a[i])
        if i + 1 >= n:
            r = i
        elif c[i + 1] == 0:
            r = i
            break
        else:
            r = i

    if l == back_l or r == back_r:
        break

    N = r - l + 1
    left = -1
    right = -1
    if l > 0:
        left = a[l - 1]

    if r < n - 1:
        right = a[r + 1]

    if N < k and M > left and M > right:
        print(-1)
        return

    if x / k <= y:
        ans += (N // k) * x
        N -= (N // k) * k
        ans += y * N
    else:

        if M < left or M < right:
            ans += y * N
        else:
            ans += x
            N -= k
            ans += y * N
    back_l = l
    back_r = r
print(ans)


'''
9 5
12 1 11
1 2 3 4 5 6 7 8 9
1 3 5 7 9
'''
