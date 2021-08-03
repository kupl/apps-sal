n = int(input())
s = bin(n)[2:]
num = len(s)
for f in s:
    if f == '1':
        print(num, end=' ')
    num -= 1
