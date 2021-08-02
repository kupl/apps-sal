A, B = list(map(int, input().split()))

ans = 0
if A >= 13:
    ans = B
elif A >= 6:
    ans = int(B / 2)
else:
    ans = 0

print(ans)
