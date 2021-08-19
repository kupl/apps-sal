(a, b) = list(map(int, input().split()))
ans = -1
for n in range(10 * b, 10 * (b + 1)):
    if int(n * 1.1) - b == int(n * 1.08) - a:
        ans = n
        break
print(ans)
