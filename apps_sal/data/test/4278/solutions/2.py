N = int(input())
dic = {}
ans = 0
for i in range(N):
    a = sorted(input())
    a = "".join(a)
    if a in dic:
        ans += dic[a]
        dic[a] += 1
    else:
        dic[a] = 1
print(ans)
