n = int(input())
L = list(map(int, input().split()))
for i in range(1, n):
    for j in range(n - i):
        if L[j] > L[j + 1]:
            (L[j], L[j + 1]) = (L[j + 1], L[j])
            print(j + 1, j + 2)
