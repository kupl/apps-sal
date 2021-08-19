n = int(input())
d = sorted(list(map(int, input().split())))
left = d[n // 2 - 1]
right = d[n // 2]
if left == right:
    ans = 0
else:
    ans = right - left
print(ans)
