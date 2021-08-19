mod = 1000000007
n = int(input())
s = input()
s2 = input()
a = [] if n > 1 else [1]
for i in range(n - 1):
    if i != 0 and s[i - 1] == s[i]:
        continue
    if s[i] == s[i + 1]:
        a.append(2)
        if i == n - 3:
            a.append(1)
    else:
        a.append(1)
        if i == n - 2:
            a.append(1)
ans = 3 if a[0] == 1 else 6
for i in range(len(a) - 1):
    (b, c) = a[i:i + 2]
    if b == 1:
        ans = ans * 2 % mod
    elif c == 2:
        ans = ans * 3 % mod
print(ans)
