n = int(input())
N = sorted(map(int, input().split()))
if n % 2 == 0:
    print(N[(n - 1) // 2])
else:
    print(N[n // 2])
