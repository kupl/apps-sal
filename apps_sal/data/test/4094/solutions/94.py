K = int(input())
res = 1
x = 0
for i in range(K):
    x += 7 * res
    x %= K
    if x % K == 0:
        print((i + 1))
        break
    res *= 10
    res %= K
else:
    print((-1))
