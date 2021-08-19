(n, m) = map(int, input().strip().split())
odd = 0
even = 0
l = list(map(int, input().strip().split()))
l1 = []
for i in range(n - 1):
    if l[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    if odd == even:
        if l[i] - l[i + 1] < 0:
            l1.append(l[i + 1] - l[i])
        else:
            l1.append(l[i] - l[i + 1])
l1.sort()
count = 0
sum1 = 0
for i in l1:
    sum1 = sum1 + i
    if sum1 <= m:
        count = count + 1
    else:
        break
print(count)
