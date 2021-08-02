n, k = list(map(int, input().split()))
x0 = list(map(int, input().split()))

x1 = [i for i in x0 if i >= 0]
x2 = list(reversed([i for i in x0 if i < 0]))
count0 = len(x1)
count1 = len(x2)
ans = float('inf')

if count1 == 0:
    print((x1[k - 1]))
elif count0 == 0:
    print((-x2[k - 1]))
else:
    if 0 in x1:
        x1.remove(0)
        k -= 1
        count0 -= 1
    for i in range(min(count0, k)):
        if count1 >= k - i - 1:
            ans = min(ans, x1[i] * 2 - x2[k - i - 2])
    for i in range(min(count1, k)):
        if count0 >= k - i - 1:
            ans = min(ans, -x2[i] * 2 + x1[k - i - 2])
    print(ans)
