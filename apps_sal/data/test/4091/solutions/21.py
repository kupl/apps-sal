(n, k) = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [[a[i], i] for i in range(n)]
b.sort(reverse=True)
b = b[:k]
b.sort(key=lambda x: x[1])
ans = 0
for i in b:
    ans += i[0]
print(ans)
prev = 0
for (iter, i) in enumerate(b):
    if iter != len(b) - 1:
        print(i[1] + 1 - prev, end=' ')
        prev = i[1] + 1
    else:
        print(n - prev)
