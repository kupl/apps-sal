(n, k) = [int(i) for i in input().split()]
s = list(input())
if len(s) == 1 and k:
    s = '0'
    k -= 1
elif int(s[0]) > 1 and k:
    k -= 1
    s[0] = '1'
i = 1
while k and i < len(s):
    if s[i] != '0':
        s[i] = '0'
        k -= 1
    i += 1
print(''.join((str(e) for e in s)))
