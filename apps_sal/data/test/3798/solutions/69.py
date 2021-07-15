n = int(input())
s = int(input())

def f(b, n):
    val = 0
    while n > 0:
        val += n % b
        n //= b
    return val

if s == n:
    print(n+1)
    return
for i in range(2, int(n**0.5) + 1):
    if(f(i, n) == s):
        print(i)
        return
ans = 10**15
for i in range(1, int(n**0.5) + 1):
    b = (n-s) // i + 1
    if b < 2:
        continue
    if f(b, n) == s:
        ans = min(ans, b)

if ans == 10**15:
    print(-1)
else:
    print(ans)
