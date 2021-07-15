for _ in range(int(input())):
    # a, b, c = map(int, input().split())
    # n = int(input())
    # arr = list(map(int, input().split()))
    s = input()
    a = s.count('1')
    b = s.count('0')
    x = min(a, b)
    if x % 2 == 0:
        print('NET')
    else:
        print('DA')

