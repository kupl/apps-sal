n = int(input())
tempre, a = list(map(int, input().split()))
heights = list(map(int, input().split()))

min_abs = 10**6
ans = -1
for i, h in enumerate(heights):
    t = tempre - 0.006 * h
    if abs(t-a) < min_abs:
        ans = i+1
        min_abs = abs(t-a)
print(ans)


