n, a, b = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
for i in range(1, n + 1):
    if i in A:
        print(1, end='')
        print(' ', end='')
    else:
        print(2, end='')
        print(' ', end='')
