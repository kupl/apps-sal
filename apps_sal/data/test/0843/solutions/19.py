n = int(input())
s = input()
numbers = list(map(int, input().split()))
a = 0
cells = []
condition = False
while True:
    if a < 0 or a >= n:
        print('FINITE')
        break
    if s[a] == '>':
        a += numbers[a]
    else:
        condition = True
        a -= numbers[a]
    if condition and a in cells:
        print('INFINITE')
        break
    cells.append(a)
