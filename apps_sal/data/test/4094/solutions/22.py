k = int(input())
if k % 2 == 0 or k % 5 == 0:
    print(-1)
else:
    exc = 0
    for i in range(1, 10 ** 8):
        exc = exc * 10 + 7
        exc = exc % k
        if exc % k == 0:
            ans = i
            break
    print(ans)
