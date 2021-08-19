s = input()
if 'm' in s or 'w' in s:
    print(0)
    quit()
Fib = [1, 1]
MOD = int(1000000000.0 + 7)
for i in range(100000):
    Fib.append((Fib[-1] + Fib[-2]) % MOD)
ans = 1
l = '.'
cnt = 0
for i in s:
    if i == l:
        cnt += 1
    else:
        if l == 'u' or l == 'n':
            ans = ans * Fib[cnt] % MOD
        l = i
        cnt = 1
if l == 'u' or l == 'n':
    ans = ans * Fib[cnt] % MOD
print(ans)
