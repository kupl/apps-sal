n = int(input())
a = list(map(int, input().split()))
c = dict()
for i in range(len(a)):
    d = a[i] - i
    if d in c:
        c[d].append(a[i])
    else:
        c[d] = [a[i]]
ans = 0
for i in c:
    ans_p = 0
    for j in c[i]:
        ans_p += j
    ans = max(ans, ans_p)
print(ans)
