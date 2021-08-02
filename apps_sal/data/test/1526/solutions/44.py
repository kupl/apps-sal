ABC = list(map(int, input().split()))
ABC.sort()
ans = 0
ans += (ABC[2] - ABC[0]) // 2
if (ABC[2] - ABC[0]) % 2 == 1:
    ans += (ABC[2] - ABC[1]) // 2
    if (ABC[2] - ABC[1]) % 2 == 1:
        ans += 1
    else:
        ans += 2
else:
    ans += (ABC[2] - ABC[1]) // 2
    if (ABC[2] - ABC[1]) % 2 == 1:
        ans += 2

print(ans)
