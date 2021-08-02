def solve():
    s = input()
    u = min(s.count('0'), s.count('1'))
    if u % 2 == 1:
        print('DA')
    else:
        print('NET')


t = int(input())
for _ in range(t):
    solve()
