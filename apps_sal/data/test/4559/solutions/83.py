input()
n = list(map(int, input().split(' ')))
ans = int(n[0])
b = n[1:]
if 0 in n:
    ans = 0
else:
    for i in b:
        ans *= int(i)
        if ans > 10 ** 18:
            ans = -1
            break
print(ans)
