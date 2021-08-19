(n, k) = [int(i) for i in input().split()]
a = [0 for i in range(n)]
for i in range(k):
    x = input()
    t = [int(i) for i in input().split()]
    for j in t:
        a[j - 1] += 1
ans = 0
for i in a:
    if i == 0:
        ans += 1
print(ans)
