n = int(input())
w = list(map(int, input().split()))
s1 = 0
s2 = 0
ans = 100
for i in range(n-1):
    s1 += w[i]
    for j in range(i+1,n):
        s2 += w[j]
    a = abs(s1 - s2)
    if ans > a:
        ans = a
    s2 = 0
print(ans)

