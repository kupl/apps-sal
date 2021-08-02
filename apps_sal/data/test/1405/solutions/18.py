from copy import *
length = int(input())
arr = list(map(int, input().split()))
d = dict()
for i in arr:
    d[i] = d.get(i, 0) + 1
ans = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if i != j:
            if arr[i] == 0 and arr[j] == 0:
                ans = max(ans, d[arr[i]])
            else:
                count = 2
                a = arr[i]
                b = arr[j]
                d[a] -= 1
                d[b] -= 1
                for k in range(100):
                    if d.get(a + b):
                        count += 1
                        d[a + b] -= 1
                        c = a + b
                        a = b
                        b = c
                    else:
                        d[a] += 1
                        d[b] += 1
                        ans = max(ans, count)
                        break
                y = count - 2
                while y > 0:
                    c = b - a
                    d[c] = d.get(c, 0) + 1
                    b = a
                    a = c
                    y -= 1
print(ans)
