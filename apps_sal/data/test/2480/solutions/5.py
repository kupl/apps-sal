(N, K) = [int(n) for n in input().split()]
A = [int(n) for n in input().split()]
count = 0
for i in range(1, N + 1):
    A[i - 1] = A[i - 1] - 1
check = {0: [0, 1, [0]]}
s = 0
for i in range(1, N + 1):
    s = (s + A[i - 1]) % K
    if s in check:
        j = check[s][0]
        l = check[s][1]
        while j < l and i - check[s][2][j] >= K:
            j += 1
        check[s][0] = j
        count += l - j
        check[s][2].append(i)
        check[s][1] = l + 1
    else:
        check[s] = [0, 1, [i]]
print(count)
