(n, k) = list(map(int, input().split()))
s = input()
s1 = [s[i] for i in range(n)]
i = 0
while k > 0 and i < n:
    c = ord(s[i])
    d1 = abs(ord('a') - c)
    d2 = abs(ord('z') - c)
    if k >= d1 >= d2:
        s1[i] = 'a'
    elif k >= d2 >= d1:
        s1[i] = 'z'
    elif c - k >= ord('a'):
        s1[i] = chr(c - k)
    else:
        s1[i] = chr(c + k)
    i += 1
    k -= max(d1, d2)
if k > 0:
    ans = -1
else:
    ans = ''.join(map(str, s1))
print(ans)
