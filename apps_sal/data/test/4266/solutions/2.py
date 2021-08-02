k, x = map(int, input().split())
ans = []
if x - k + 1 < -1000000:
    for i in range(-1000000, x + k):
        ans.append(i)
elif x + k - 1 > 1000000:
    for i in range(x - k + 1, 1000001):
        ans.append(i)
else:
    for i in range(x - k + 1, x + k):
        ans.append(i)
print(' '.join(map(str, ans)))
