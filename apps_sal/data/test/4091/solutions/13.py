n, k = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

res = sorted(a, reverse=True)
res = res[0:k]
print(sum(res))
s = res
prev = 0
counter = 1
for i in range(len(a)):
    if a[i] in s:
        s.pop(s.index(a[i]))
        if counter == k:
            print(n - prev)
        else:
            print(i + 1 - prev, end=' ')
        counter += 1
        prev = i + 1
