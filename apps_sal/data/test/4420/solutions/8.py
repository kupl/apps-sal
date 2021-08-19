tt = int(input())
for loop in range(tt):
    (x, y, n) = list(map(int, input().split()))
    tmp = n // x * x + y
    if tmp > n:
        tmp -= x
    print(tmp)
