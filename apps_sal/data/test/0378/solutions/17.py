(n, r) = list(map(int, input().split()))
i = 1
m = n
while m % 10 != r and m % 10 != 0:
    m += n
    i += 1
print(i)
