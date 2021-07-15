N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))
right = 0
left = 0

for a in A:
    if X > a:
        right += 1
    elif X < a:
        left += 1

print((min(right, left)))



