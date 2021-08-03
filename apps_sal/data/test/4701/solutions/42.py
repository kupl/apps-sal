ans = float('inf')
n, k = int(input()), int(input())
for i in range(2**n):
    ans = min(ans, eval('(' * n + '1' + "".join('*2)'if (i >> j) % 2 else '+' + str(k) + ')' for j in range(n))))
print(ans)
