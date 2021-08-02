t = int(input())
for i in range(t):
    n, x = list(map(int, input().split()))
    A = [int(j) for j in input().split()]
    A = set(A)
    j = 1
    while True:
        if j in A:
            j += 1
        else:
            if x == 0:
                break
            x -= 1
            j += 1
    print(j - 1)
