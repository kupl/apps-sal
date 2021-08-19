(num_cows, num_boxes) = list(map(int, input().split()))
cows = list(map(int, input().split()))
need = cows[-1]
limit = 2 * (num_cows - num_boxes)
for left in range(limit):
    right = limit - 1 - left
    if right < left:
        break
    need = max(need, cows[left] + cows[right])
print(need)
