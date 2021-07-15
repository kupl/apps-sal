n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []
for i in range (0, n) :
    c.append(a[i] - b[i])
c.sort()
p1 = n - 1
p2 = 0
ans = 0
while p1 > p2 :
    while p2 < p1 and c[p1] + c[p2] <= 0 :
        p2 += 1
    ans += p1 - p2
    # print(ans)
    p1 -= 1
print(ans)
