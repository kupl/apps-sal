n = int(input())
a = [int(s) for s in input().split()]
ans = 0
parity = True
while parity:
    for i in range(n):
        if a[i] % 2 == 0:
            a[i] = a[i] / 2
        else:
            parity = False
    if parity:
        ans += 1
print(ans)
