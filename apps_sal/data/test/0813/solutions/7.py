def read():
    return map(int, input().split())


(n, a, b) = read()
p1 = list(read())
p2 = list(read())
ans = [0] * n
for x in p1:
    ans[x - 1] = 1
for x in p2:
    if ans[x - 1] == 0:
        ans[x - 1] = 2
print(' '.join(map(str, ans)))
