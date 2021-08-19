import collections
t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    x = 0

    D = [k - a[i] % k for i in range(n) if a[i] % k]
    D.sort(reverse=True)
    ans = 0
    if len(D):
        C = collections.Counter(D).most_common()
        # print(C)
        ans = (C[0][1] - 1) * k + C[0][0] + 1

    print(ans)
