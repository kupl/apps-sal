x, y = list(map(int, input().split()))
ans = 'No'
if y % 2 == 0 and y >= x*2 and y <= x*4:
    ans = 'Yes'
print(ans)

