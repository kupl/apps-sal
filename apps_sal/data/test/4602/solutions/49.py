N = int(input(''))
K = int(input(''))
a = input('').split(' ')
a = [int(aa) for aa in a]
ans = 0
for x in a:
    if K - x < x:
        ans += (K - x) * 2
    elif K - x >= x:
        ans += x * 2
print(ans)
