n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    b.append([a[i], -i])
b.sort(reverse=True)
for i in range(int(input())):
    (k, pos) = map(int, input().split())
    ans = 0
    z = []
    for i in range(k):
        ans += b[i][0]
        z.append([-b[i][1], b[i][0]])
    z.sort()
    print(z[pos - 1][1])
