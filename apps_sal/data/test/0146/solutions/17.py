n, k = map(int, input().split())
l = list(map(int, input().split()))
e, s = 0, 0
for i in l:
    if i == 1:
        e += 1
    else:
        s += 1
ans = 0
for i in range(k):
    e1, s1 = e, s
    for j in range(i, n, k):
        if l[j] == 1:
            e1 -= 1
        else:
            s1 -= 1
    ans = max(ans, abs(e1 - s1))
print(ans)
