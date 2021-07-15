A, B = map(int, input().split())
if A < 6:
    ans = 0
elif A <= 12:
    ans = int(B / 2)
else:
    ans = B
print(ans)
