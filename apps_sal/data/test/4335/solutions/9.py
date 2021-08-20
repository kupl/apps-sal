n = int(input())
s = input()
t = s[:int(n / 2)]
if s == t + t:
    print('Yes')
else:
    print('No')
