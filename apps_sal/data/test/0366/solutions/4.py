(n, s) = list(map(int, input().split()))
if s % n == 0:
    print(s // n)
else:
    print(s // n + 1)
