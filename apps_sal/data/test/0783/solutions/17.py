# -*- coding: utf-8 -*-

n = int(input())
houses = list(map(int, input().split()))
height = [0]
result = []

for i in range(n):
    if houses[n - i - 1] > height[i]:
        height.append(houses[n - i - 1])
        result.append(0)
    else:
        height.append(height[i])
        result.append(height[i] - houses[n - i - 1] + 1)

for i in range(n):
    print(result[n - i - 1], end=' ')
