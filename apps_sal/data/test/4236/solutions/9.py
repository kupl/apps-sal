n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
ans = 0
answ = []
for i in range(1, m + 1):
    flag = False
    for elem in a:
        flag |= elem[0] <= i <= elem[1]
    ans += not flag
    if not flag:
        answ.append(i)
print(ans)
print(*answ)
