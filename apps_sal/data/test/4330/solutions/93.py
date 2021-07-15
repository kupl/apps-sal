a, b = map(int, input().split())
ans = (a**2-b**2)/(2*(a-b))

if ans.is_integer():
    print(int(ans))
else:
    print('IMPOSSIBLE')
