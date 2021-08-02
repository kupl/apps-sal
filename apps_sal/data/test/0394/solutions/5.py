n = int(input())
a = [int(k) for k in input().split()]
answ = []
for k in range(1, n + 1):
    prev = 0
    arr = [0 for i in range(k)]
    good = True
    for i in range(n):
        if i < k:
            arr[i] = a[i] - prev
        else:
            if arr[i % k] != a[i] - prev:
                good = False
                break
        prev = a[i]
    if good:
        answ.append(k)
print(len(answ))
print(*answ)
