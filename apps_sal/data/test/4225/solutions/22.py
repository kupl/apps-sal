def main():
    a, b, c, k = list(map(int, input().split()))

    sum = 0

    n = k-a
    if n <= 0:
        sum = k
        print(sum)
        return
    else:
        sum = a

    n = n-b
    if n <= 0:
        print(sum)
        return
    
    n = n-c
    if n <= 0:
        sum = sum - (k-(a+b))
        print(sum)
        return

main()

