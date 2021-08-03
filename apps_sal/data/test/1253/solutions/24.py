n, k = list(map(int, input().split()))
a = list(map(int, input().split()))
count = 0
count1 = 0
for i in a:
    if i < 0:
        count1 += 1
if k <= count1:
    for i in range(k):
        a[i] = -a[i]
    print(sum(a))
elif (count1 - k) % 2 == 0:
    for i in range(count1):
        a[i] = -a[i]
    print(sum(a))
else:
    for i in range(count1):
        a[i] = -a[i]
    m = min(a)
    a.remove(m)
    a.append(-m)
    print(sum(a))
