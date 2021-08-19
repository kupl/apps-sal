n = int(input())
arr = dict()
k = set()
for h in range(2, n + 1):
    i = h
    for j in range(2, int(-(-i ** 0.5 // 1)) + 1):
        if i % j == 0:
            cnt = 0
            while i % j == 0:
                cnt += 1
                i //= j
            if j not in arr:
                arr[j] = cnt
                k.add(j)
            else:
                arr[j] += cnt
    if i != 1:
        if i in arr:
            arr[i] += 1
        else:
            arr[i] = 1
        k.add(i)
ans = 1
for num in k:
    ans *= arr[num] + 1
    ans = ans % (10 ** 9 + 7)
print(ans)
