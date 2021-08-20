(n, t) = [int(x) for x in input().split()]
(a, s) = input().split('.')
s = list(s)
pos = len(s) - 1
for i in range(len(s)):
    if ord(s[i]) > ord('4'):
        pos = i
        break
while t > 0 and pos > 0:
    if ord(s[pos]) > ord('4'):
        pos -= 1
        s[pos] = chr(ord(s[pos]) + 1)
        t -= 1
    else:
        break
if t > 0 and pos == 0 and (s[0] > '4'):
    it = len(a) - 1
    A = [ord(ch) - ord('0') for ch in a]
    A[it] += 1
    while it > 0:
        if A[it] == 10:
            A[it] = 0
            A[it - 1] += 1
            it -= 1
        else:
            break
    res = ''.join([str(x) for x in A])
    print(res)
else:
    res = a + '.' + ''.join(s[:pos + 1])
    print(res)
