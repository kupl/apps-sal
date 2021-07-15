N, W = (int(i) for i in input().split())
L = [int(i) for i in input().split()]

n = 0
left = 0
right = W

for i in L:
    n += i
    if n + right > W:
        right -= n + right - W
    if n + left < 0:
        left += -(n + left)

print(max(right - left + 1, 0))

