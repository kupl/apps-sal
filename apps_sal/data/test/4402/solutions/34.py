def LI():
    return list(map(int, input().split()))


A, B = LI()
if A >= 13:
    ans = B
elif A > 5:
    ans = B//2
else:
    ans = 0
print(ans)

