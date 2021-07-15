a, b, c, d = (int(x) for x in input().split())
if a+b > c+d:
    ans = 'Left'
elif a+b < c+d:
    ans = 'Right'
else:
    ans = 'Balanced'
print(ans)
