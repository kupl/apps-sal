for it in range(1, int(input()) + 1):
    n = int(input())
    s = input()
    if s.count('0') > s.count('1'):
        print('0' * n)
    else:
        print('1' * n)

