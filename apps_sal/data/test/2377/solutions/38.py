n, h = list(map(int, input().split()))
num = []
for i in range(n):
    a, b = list(map(int, input().split()))
    num.append([a, 0])
    num.append([b, 1])
num.sort(reverse=True, key=lambda x: x[0])
ans = 0
for i in range(n * 2):
    if num[i][1] == 1:
        ans += 1
        h -= num[i][0]
        if h <= 0:
            break
    else:
        ans += -(h // -num[i][0])
        break
print(ans)
