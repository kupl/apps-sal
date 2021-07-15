n, a, b = map(int, input().split())
c = list(map(int, input().split()))
count = 0
ans = "YES"
for i in range(n // 2):
    if c[i] == 2:
        if c[-(i + 1)] == 2:
            count += min(a, b) * 2
        elif c[-(i + 1)] == 0:
            count += a
        elif c[-(i + 1)] == 1:
            count += b
    elif c[i] == 0:
        if c[-(i + 1)] == 2:
            count += a
        elif c[-(i + 1)] == 0:
            count += 0
        elif c[-(i + 1)] == 1:
            ans = "NO"
            break
    elif c[i] == 1:
        if c[-(i + 1)] == 2:
            count += b
        elif c[-(i + 1)] == 1:
            count += 0
        elif c[-(i + 1)] == 0:
            ans = "NO"
            break
if n % 2 == 1 and c[n // 2] == 2:
    count += min(a, b)
if ans == "NO":
    print(-1)
else:
    print(count)
