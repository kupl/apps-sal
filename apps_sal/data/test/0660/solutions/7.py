n, b, p = map(int, input().split())
m = n
ans = 0
while m > 1:
    lb = 0
    rb = 10
    while lb != rb:
        mb = (lb + rb + 1) // 2
        if 2**mb <= m:
            lb = mb
        else:
            rb = mb - 1
    ans += (2**lb) * b + 2**(lb - 1)
    m -= 2**(lb - 1)
print(ans, n * p)
