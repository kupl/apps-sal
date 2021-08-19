(a, b) = map(int, input().split())
li = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
ans = 0
for i in range(a, b + 1):
    for x in list(str(i)):
        ans += li[int(x)]
print(ans)
