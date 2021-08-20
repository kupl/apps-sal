(n, s) = list(map(int, input().split()))
num_1 = s // n
if s % n == 0:
    print(num_1)
else:
    print(num_1 + 1)
