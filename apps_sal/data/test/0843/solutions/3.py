n = int(input())
s = input()
num = list(map(int, input().split()))
pos = 0
b = [True] * n
while n > pos >= 0 and b[pos]:
    b[pos] = False
    if s[pos] == '>':
        pos += num[pos]
    else:
        pos -= num[pos]
if n > pos >= 0:
    print('INFINITE')
else:
    print('FINITE')
