n = int(input())
h = list(map(int,input().split()))
cnt = []
right = 0
for left in range(n):
    while right<n-1 and h[right] >= h[right+1]:
        right += 1
    cnt.append(right-left)
    if right==left:
        right += 1
print(max(cnt))
