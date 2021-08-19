def divi(n):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return l


n = int(input())
s = input()
sl = [i for i in s]
l = divi(n)
for i in l:
    x = sl[:i]
    sl[:i] = x[::-1]
ans = ''
for i in sl:
    ans += i
print(ans)
