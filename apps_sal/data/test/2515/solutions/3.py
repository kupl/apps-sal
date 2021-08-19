def isPrime(x):
    ans = True
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            ans = False
            break
    return ans


q = int(input())
queries = []
rMax = 1
for i in range(q):
    (l, r) = list(map(int, input().split()))
    queries.append((l, r))
    rMax = max(rMax, r)
cnt = [0] * (rMax + 1)
for i in range(2, (rMax + 1) // 2 + 1):
    cnt[2 * i - 2] = cnt[2 * i - 3]
    if isPrime(i) and isPrime(2 * i - 1):
        cnt[2 * i - 1] = cnt[2 * i - 2] + 1
    else:
        cnt[2 * i - 1] = cnt[2 * i - 2]
for (l, r) in queries:
    print(cnt[r] - cnt[l - 1])
