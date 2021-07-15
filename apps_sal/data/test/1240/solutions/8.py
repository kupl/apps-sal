n = int(input())
coloms = [[None, None] for i in range(n)]
for i in range(n):
    coloms[i][0], coloms[i][1] = list(map(int, input().split()))
left_men = sum([t[0] for t in coloms])
right_men = sum([t[1] for t in coloms])
beauty = abs(left_men - right_men)
first = beauty
ans = 0
for i in range(n):
    colom = coloms[i]
    new_beauty = abs((left_men - colom[0] + colom[1]) - (right_men - colom[1] + colom[0]))
    if new_beauty > beauty:
        ans = i + 1
        beauty = new_beauty
print(ans)

