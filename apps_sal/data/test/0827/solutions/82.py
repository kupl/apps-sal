n = int(input())
t = input()
p = '110' * (n // 3 + 2)
if p[:n] != t and p[1:n + 1] != t and (p[2:n + 2] != t):
    ans = 0
elif t == '1':
    ans = 2 * 10 ** 10
elif t == '11':
    ans = 10 ** 10
else:
    k = 0
    for c in t:
        if c == '0':
            k += 1
    if t[-1] == '0':
        ans = 10 ** 10 - (k - 1)
    else:
        ans = 10 ** 10 - k
print(ans)
