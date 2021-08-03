x = int(input())
ans = 0
i = 0
while True:
    i += 1
    x -= i
    ans += 1
    if x <= 0:
        break
print(ans)
