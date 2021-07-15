def mi():
        return list(map(int, input().split()))
'''
4
5
4 3 1 4 5
4
4 4 4 4
3
1 1 1
5
5 5 1 1 5
'''
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(mi()))[::-1]
    ans = -1
    mintillnow = 1e99
    for i in range(n):
        mintillnow = min(mintillnow, a[i])
        ans = max(ans, min(i+1, mintillnow))
    print(ans)

