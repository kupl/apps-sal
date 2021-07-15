n = input()

ans = tmp = 0.0

pd = 1.0

for i in reversed(sorted(map(float, input().split()))):

    tmp = tmp * (1.0 - i) + pd * i

    pd *= 1.0 - i

    ans = max(ans, tmp)

print('%0.12f' % ans)



# Made By Mostafa_Khaled

