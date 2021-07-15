n = int(input())

ans = ['o' for _ in range(n)]
fib = [0, 1]
while fib[-1] < n:
    fib.append(fib[-2] + fib[-1])
for i in fib:
    if 0 < i <= n:
        ans[i - 1] = 'O'
print(''.join(ans))

