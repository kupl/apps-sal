(a, b) = map(int, input().split())
ans = -1
for i in range(0, 10000):
    if int(i * 0.08) == a and int(i * 0.1) == b:
        ans = i
        break
print(ans)
