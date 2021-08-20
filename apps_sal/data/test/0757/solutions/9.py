s = input().split()
n = int(s[0])
m = int(s[1])
k = int(s[2])
a = []
mp = list(map(int, input().split()))
for j in mp:
    a.append(j)
a.sort(reverse=True)
if k >= m:
    print(0)
else:
    ans = -1
    count = 0
    total = 0
    sum = 0
    for j in range(n):
        count += 1
        sum += a[j]
        total = k - count + sum
        if total >= m:
            break
    if total >= m:
        ans = count
    print(ans)
