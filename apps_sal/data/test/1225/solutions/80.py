h = int(input())
ans = 0
for i in range(10 ** 10):
    if h == 1:
        print(2 ** (ans + 1) - 1)
        break
    else:
        h //= 2
        ans += 1
