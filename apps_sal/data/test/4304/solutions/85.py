(a, b) = map(int, input().split())
dif = b - a
temp = 0
for i in range(dif):
    temp += i
ans = temp - a
print(ans)
