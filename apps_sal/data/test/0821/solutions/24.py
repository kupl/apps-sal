(s, v1, v2, t1, t2) = (int(x) for x in input().split())
ans1 = t1 * 2 + s * v1
ans2 = t2 * 2 + s * v2
if ans1 < ans2:
    ans = 'First'
elif ans1 == ans2:
    ans = 'Friendship'
else:
    ans = 'Second'
print(ans)
