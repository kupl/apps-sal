x = int(input())
ans = 0
val = 100
while 1:
    ans += 1
    val += val // 100
    if val >= x:
        break
print(ans)

