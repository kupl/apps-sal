n, m = list(map(int, input().split()))
remain = set(range(1, m + 1))
for _ in range(n):
    l, r = list(map(int, input().split()))
    for i in range(l, r + 1):
        remain.discard(i)

print(len(remain))
print(*sorted(remain))
