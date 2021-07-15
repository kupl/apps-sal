n = int(input())
a = list()
f = []
for i in range(n):
    cur = [list(map(int, input().split())), i + 1]
    if cur[0][0] < cur[0][1]:
        f.append(cur)
    else:
        a.append(cur)
if len(f) >= n // 2:
    f.sort(key=lambda x: x[0][0], reverse=True)
    print(len(f))
    ans = ''
    for i in f:
        ans += str(i[1]) + ' '
    print(ans)
else:
    a.sort(key=lambda x: x[0][0], reverse=False)
    print(len(a))
    ans = ''
    for i in a:
        ans += str(i[1]) + ' '
    print(ans)

