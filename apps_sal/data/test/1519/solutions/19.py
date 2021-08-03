n, l, a = map(int, input().split())
time = 0

t = []
ans = 0

for i in range(n):

    b = list(map(int, input().split()))
    t.append(b)

for i in range(n):

    if t[i][0] > time:

        ans += (t[i][0] - time) // a
        time = t[i][0] + t[i][1]
    else:
        time = t[i][0] + t[i][1]

if l > time:
    ans += (l - time) // a

print(ans)
