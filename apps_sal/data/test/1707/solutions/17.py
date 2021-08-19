n = int(input())
L = sorted([abs(int(x)) for x in input().split()])
T = 0
for i in range(n - 1):
    (l, h) = (i, n - 1)
    while h != l:
        if L[(l + h + 1) // 2] <= 2 * L[i]:
            l = (l + h + 1) // 2
        else:
            h = (l + h) // 2
    T += l - i
print(T)
