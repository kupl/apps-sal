num = int(input())
ans = 0
while(num != 0):
    L = list(str(num))
    d = int(max(L))
    num -= d
    ans += 1
print(ans)
