n, k = map(int, input().split(" "))
if k == 1:
    print(n)

else:
    num = 1
    while num <= n:
        num <<= 1

    print(num - 1)
