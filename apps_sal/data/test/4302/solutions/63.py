A, B = list(map(int, input().split()))
total = 0

if A == B:
    total = A * 2
else:
    total = max(A, B) * 2 - 1

print(total)
