(n, k) = list(map(int, input().split()))

lst = []
for x in input().split():
    lst.append(int(x))

r = n + 1
for x in range(len(lst)):
    if n % lst[x] < r:
        r = n % lst[x]
        t = x

print(t + 1, n // lst[t])
