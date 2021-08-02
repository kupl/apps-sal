def resolve():
    n = int(input())
    s = input()
    if s == s[:n // 2] + s[:n // 2]:
        print('Yes')
    else:
        print('No')


resolve()
