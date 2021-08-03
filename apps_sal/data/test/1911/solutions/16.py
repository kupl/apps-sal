n, k = map(int, input().split())
l = list(map(int, input().split()))
cost = l[n - 1] - l[0]
if k == 1:
    print(cost)
else:
    diff = [0 for _ in range(n - 1)]
    for i in range(n - 1):
        diff[i] = l[i + 1] - l[i]
    # print(diff)
    diff = sorted(diff)
    diff.reverse()
    print(cost - sum(diff[:k - 1]))
