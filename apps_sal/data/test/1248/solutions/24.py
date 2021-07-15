lst = [int(x) for x in input().split()]
ans = lst[0] + lst[1] + lst[2]
ans = min(ans, 2 * lst[0] + 2 * lst[1])
ans = min(ans, 2 * lst[0] + 2 * lst[2])
ans = min(ans, 2 * lst[1] + 2 * lst[2])
print(ans)
