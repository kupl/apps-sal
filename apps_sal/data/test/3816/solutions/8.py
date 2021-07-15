a, b, c, l = list(map(int, input().split()))

ans = (l + 3) * (l + 2) * (l + 1) // 3

for z in (a, b, c):

    s = 2 * z - a - b - c

    for x in range(max(0, -s), l + 1):

        m = min(s + x, l - x)

        ans -= (m + 1) * (m + 2)

print(ans // 2)



# Made By Mostafa_Khaled

