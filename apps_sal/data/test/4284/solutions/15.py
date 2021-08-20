T = int(input())
test = 0
while test < T:
    arr = input()
    (K, N, a, b) = [int(num) for num in arr.split(' ')]
    if N * b >= K:
        print(-1)
    else:
        s = N * b
        d = a - b
        m = (K - 1 - s) // d
        if m <= N:
            print(m)
        else:
            print(N)
    test += 1
