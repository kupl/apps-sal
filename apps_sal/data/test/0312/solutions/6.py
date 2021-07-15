n, m = list(map(int, input().split()))
if n == 1 and m == 1:
    print(1)
elif n - m > m - 1:
    print(m+1)
else:
    print(m-1)
