def read(): return [int(i) for i in input().split()]


t = int(input())
while t > 0:
    t -= 1
    s = input()
    s_sort = sorted(s)
    if s_sort[0] == s_sort[-1]:
        print(-1)
    else:
        print(''.join(s_sort))
