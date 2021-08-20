def mi():
    return list(map(int, input().split()))


'\n4\n5\n4 3 1 4 5\n4\n4 4 4 4\n3\n1 1 1\n5\n5 5 1 1 5\n'
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(mi()))[::-1]
    ans = -1
    mintillnow = 1e+99
    for i in range(n):
        mintillnow = min(mintillnow, a[i])
        ans = max(ans, min(i + 1, mintillnow))
    print(ans)
