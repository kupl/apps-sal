n = int(input())
h = list(map(int, input().split()))
ans = 'Yes'
for i in range(2, n + 1):
    if h[-i] <= h[-(i - 1)]:
        continue
    elif h[-i] == h[-(i - 1)] + 1:
        h[-i] -= 1
    else:
        ans = 'No'
print(ans)
