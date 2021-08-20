for i in range(int(input())):
    (a0, a1, a2) = list(map(int, input().split()))
    (b0, b1, b2) = list(map(int, input().split()))
    twos = min(a2, b1)
    a2 -= twos
    b1 -= twos
    zeros = min(a1, b0 + b1)
    a1 -= zeros
    ones = min(a1, b2)
    print(twos * 2 - ones * 2)
