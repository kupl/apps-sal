n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
if n % 2 == 0:
    a = n // 2 - 1
    s = lst[0]
    for i in range(a):
        s += 2 * (lst[i + 1])

else:
    b = (n - 1) // 2
    s = lst[0]
    for j in range(b):
        s += 2 * (lst[j + 1])
    s -= lst[b]

print(s)
