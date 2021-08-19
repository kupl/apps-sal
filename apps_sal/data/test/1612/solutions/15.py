n = int(input())
a = []
for i in range(n):
    li = list(map(int, input().split()))
    a.append(set(li[1:]))
for i in range(n):
    s = a[i]
    joke = 1
    for j in range(n):
        t = a[j]
        if t <= s and i != j:
            joke = 0
            break
    print('YES' * joke + 'NO' * (1 - joke))
