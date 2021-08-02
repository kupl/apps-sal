S, P = map(int, input().split())


def yakusu(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n != i**2:
                ans.append(n // i)
#    ans.sort()
    return ans


y = yakusu(P)

ans = False
for yy in y:
    if yy + P // yy == S:
        ans = True
        break
if ans:
    print("Yes")
else:
    print("No")
