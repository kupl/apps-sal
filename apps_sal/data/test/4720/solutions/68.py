n = int(input())
count = 0
for _ in range(n):
    (l, r) = map(int, input().split())
    count += r - l + 1
print(count)
