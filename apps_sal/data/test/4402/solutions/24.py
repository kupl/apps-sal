A, B = map(int, input().split())

ans = 0
if A >= 13:
    ans = B
elif 12 >= A >= 6:
    ans = B // 2

print(ans)
