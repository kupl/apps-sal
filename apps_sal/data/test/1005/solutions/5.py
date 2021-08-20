INT_MAX = int(1000000000.0 + 7)
t = int(input())
for _ in range(t):
    (n, k, d) = list(map(int, input().split(' ')))
    a = list(map(int, input().split(' ')))
    ans = INT_MAX
    for i in range(len(a) - d + 1):
        ans = min(ans, len(set(a[i:i + d])))
    print(ans)
