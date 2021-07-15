a = input()

n = len(a)
ans = 0
for i in range(2**(n-1)):
    f = a[0]
    for j in range(n-1):
        if ((i >> j) & 1):
            f += '+'
        f += a[j+1]

    ans += sum(map(int, f.split('+')))

print(ans)
