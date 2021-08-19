n = int(input())
l = list(map(int, input().split()))
temp = []
for i in l:
    temp.append(len(bin(i & -i)[2:]))
f = [0] * 61
for i in temp:
    f[i] += 1
cmp = f.index(max(f))
ans = []
for i in range(n):
    if temp[i] != cmp:
        ans.append(l[i])
print(len(ans))
print(*ans)
