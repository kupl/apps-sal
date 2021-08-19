n = int(input())
A = list(map(int, input().split()))
A.sort()
judge = 0
if n % 2 == 1:
    for i in range(n):
        if A[i] != 2 * ((i + 1) // 2):
            judge += 1
            break
else:
    for i in range(n):
        if A[i] != 2 * (i // 2) + 1:
            judge += 1
            break
if judge == 1:
    print(0)
else:
    print(2 ** (n // 2) % (10 ** 9 + 7))
