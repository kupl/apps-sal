n = int(input())
a = [int(input()) for _ in range(5)]
if n % min(a) != 0:
    n += min(a) - n % min(a)
if min(a) >= n:
    print(5)
else:
    print(int(n / min(a)) + 4)
