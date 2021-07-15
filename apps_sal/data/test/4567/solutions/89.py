N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))
sum1 = sum(ls)
ls.sort()
ans = 0
if sum1 % 10 != 0:
    ans = sum1
else:
    for i in range(N):
        if (sum1-ls[i]) % 10 != 0:
            ans = sum1-ls[i]
            break
print(ans)
