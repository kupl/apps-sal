def deep(n):
    if n != 0:
        i = 0
        while n > 2**i:
            i += 1
        if n == 2**i:
            print(i+1)
        else:
            print(i, end=' ')
            n -= 2**(i-1)
            deep(n)

n = int(input())
deep(n)

