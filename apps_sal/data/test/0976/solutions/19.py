n, x = list(map(int, input().split()))
left = 1
total = 0
for _ in range(n):

    l, r = list(map(int, input().split()))
    total += (l - left) % x + (r - l + 1)
    left = r + 1

print(total)

