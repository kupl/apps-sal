def solve(a):
    b = sorted(a)
    N = len(b)
    if N % 2 == 0:
        if b[::2] == b[1::2]:
            return 'Second'
        else:
            return 'First'
    else:
        return 'Second'


for _ in range(int(input())):
    N = input()
    print(solve(list(map(int, input().split()))))
