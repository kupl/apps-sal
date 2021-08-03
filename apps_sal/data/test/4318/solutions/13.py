N = int(input())
height = list(map(int, input().split()))

count = 1
max_height = height[0]

for i in range(1, N):
    if height[i] >= max_height:
        max_height = height[i]
        count += 1

print(count)
