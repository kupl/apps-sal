n = int(input())
s = input().split()
a = []
b = []
for i in range(2*n):
    a.append(int(s[i]))
a.sort()
for i in range(len(a)):
    b.append(str(a[i]) + ' ' + str(a[-i-1]))
for i in range(n):
    print(''.join(b[i]))





