N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

count = 0
for a in A:
    if a >= sum(A) / 4 / M:
        count += 1

print("Yes" if count >= M else "No")
