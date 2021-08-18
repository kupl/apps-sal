n, d = map(int, input().split())

cover_area = (d * 2 + 1)
ans = n // cover_area
if (n % cover_area) != 0:
    print(ans + 1)
else:
    print(ans)
