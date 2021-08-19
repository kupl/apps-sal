n = int(input())
L = list(map(int, input().split()))
if n % 2 == 0:
    A = L[n - 1::-2] + L[::2]
else:
    A = L[n - 1::-2] + L[1::2]
print(*A)
