n = int(input())
blue = [input() for i in range(n)]
m = int(input())
red = [input() for i in range(m)]
ans = 0
for i in range(n):
    tmp = blue.count(blue[i]) - red.count(blue[i])
    ans = max(ans, tmp)
print(ans)
