def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = "NO"
    d = {}
    for i in range(n):
        if a[i] not in d: d[a[i]] = i
        elif i - 1 > d[a[i]]: ans = "YES"
    return ans


for _ in range(int(input())):
    print(solve())
