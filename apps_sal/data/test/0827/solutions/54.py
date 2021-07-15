import sys
n = int(input())
s = input()

M = 10000000000

if s == '1':
    print((2 * M))
    return
elif s == '0':
    print(M)
    return
else:
    for i in range(n-1):
        if s[i] == '0' and s[i+1] == '0':
            print((0))
            return
    for i in range(n-2):
        if s[i] == '1' and s[i+1] == '1' and s[i+2] == '1':
            print((0))
            return
        elif s[i] == '0' and s[i+1] == '1' and s[i+2] == '0':
            print((0))
            return

if s[-1] == '0':
    m = s.count('0')
    print((M - (m - 1)))
else:
    m = s.count('0') + 1
    print((M - (m - 1)))


