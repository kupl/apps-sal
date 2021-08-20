prime = [0, 0] + [1] * (10 ** 5 - 1)
for x in range(2, 5 * 10 ** 2 + 1):
    if prime[x]:
        for i in range(2, 10 ** 5 // x + 1):
            prime[x * i] = 0
islike2017 = [0] * (10 ** 5 + 1)
cnt = 0
for z in range(2, 10 ** 5 + 1):
    if prime[z] and prime[(z + 1) // 2]:
        cnt += 1
    islike2017[z] = cnt
Q = int(input())
for _ in range(Q):
    (l, r) = map(int, input().split())
    print(islike2017[r] - islike2017[l - 1])
