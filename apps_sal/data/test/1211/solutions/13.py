n, k = list(map(int, input().split()))
L = list(map(int, input().split()))
ans = 0
box = 0
for i in range(k):
    new = n // L[i] * L[i]
    if new > ans:
        ans = new
        box = i
print(box + 1, n // L[box])
