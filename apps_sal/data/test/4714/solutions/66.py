def kaibun(n):
    if str(n)[0] == str(n)[-1] and str(n)[1] == str(n)[-2]:
        return True
    else:
        return False


a, b = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    if kaibun(i):
        ans += 1
print(ans)
