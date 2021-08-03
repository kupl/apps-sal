a, b = map(int, input().split())
ans = -1
for i in range(11000):
    if int(i * 1.08) == i + a and int(i * 1.1) == i + b:
        ans = i
        break
print(ans)
