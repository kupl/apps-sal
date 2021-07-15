# A - Favorite Sound

A, B, C = list(map(int, input().split()))

# A enn B kai MAX c

if A * C <= B:
    answer = C
else:
    answer = B // A

print(answer)

