(x, y, a, b, c) = map(int, input().split())
red = list(map(int, input().split()))
green = list(map(int, input().split()))
colorless = list(map(int, input().split()))
temp = []
red.sort(reverse=True)
green.sort(reverse=True)
colorless.sort(reverse=True)
for i in range(min(x, a)):
    temp.append(red[i])
for i in range(min(y, b)):
    temp.append(green[i])
for i in range(c):
    temp.append(colorless[i])
temp.sort(reverse=True)
ans = 0
for i in range(x + y):
    ans += temp[i]
print(ans)
