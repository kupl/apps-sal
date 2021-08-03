n = int(input())
w = list(map(int, input().split()))

total_w = 0
for i in w:
    total_w += i

half_w = total_w / 2

front_w = 0
idx = 0
for i in range(n):
    idx = i
    front_w += w[idx]
    if front_w >= half_w:
        break
    else:
        pass

print(int(2 * min(front_w - half_w, half_w - front_w + w[idx])))
