ABC = list(map(int,input().split()))
ans = 0
ABC.sort()
if ABC[0] == ABC[1] == ABC[2]:
    ans = 0
elif ABC[0] != ABC[1] and ABC[1] != ABC[2]:
    sa = ABC[2] - ABC[1]
    ans += sa
    ABC[0] += sa
    ans += -(-(ABC[2] - ABC[0])//2)
    if (ABC[2] - ABC[0]) % 2 == 1:
        ans += 1
elif ABC[0] == ABC[1]:
    ans += ABC[2] - ABC[0]
elif ABC[1] == ABC[2]:
    ans += -(-(ABC[2]-ABC[0])//2)
    if (ABC[2] - ABC[0]) % 2 == 1:
        ans += 1
print(ans)

