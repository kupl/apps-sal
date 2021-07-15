def get_n(n, k):
    if bin(n).count('1') > k or k > n:
        return False
    return True

n, p = list(map(int, input().split()))

if p - n >= 0:
    print(-1)
elif p - n == -1:
    print(1)
else:
    for i in range(1, 10101):
        if get_n(n - p * i, i):
            print(i)
            return
    print(-1)

