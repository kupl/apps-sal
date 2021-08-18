N, K = map(int, input().split())
A = list(map(int, input().split()))

check = [0] * (N + 1)
li = []
i, j = 1, 1

while True:
    k = A[i - 1]
    if check[k] == 1:
        n = li.index(k) + 1
        break
    check[k] = 1
    li.append(k)
    i = k
    j += 1

if K < n:
    print(li[K - 1])
else:
    print(li[(K - n) % (j - n) + n - 1])
