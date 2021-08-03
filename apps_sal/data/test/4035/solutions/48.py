a, b = map(int, input().split())
i = 0
x = int(a / 0.08)
while True:
    if int((x + i) * 0.1) == b and int((x + i) * 0.08) == a:
        ans = int(x + i)
        break
    elif int((x + i) * 0.1) > b:
        ans = '-1'
        break
    else:
        i += 1
print(ans)
