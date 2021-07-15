a, b = map(int, input().split())
c = (a * b) % 2

if c == 0:
    print('Even')
elif c == 1:
    print('Odd')
