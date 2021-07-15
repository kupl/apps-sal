import math
a = list(map(int, input().split()))
a.sort()
diff = a[1] - a[0]

yakusuu = []
for i in range(1, int(diff**(1/2))+1):
    if diff % i == 0:
        yakusuu.append(i)
        yakusuu.append(diff//i)

yakusuu.sort()
ans = [[a[0]*a[1], 0]]

for i in yakusuu:
    x = a[0]
    y = a[1]
    k = 0
    if x % i != 0:
        k = i - x % i

    x += k
    y += k
    anstemp = (x*y//math.gcd(x, y))
    ans.append([anstemp, k])

ans.sort()
print(ans[0][1])

