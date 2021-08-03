n = int(input())
s = input()
perm = ["RGB", "RBG", "BRG", "BGR", "GRB", "GBR"]
ans = 0

ans = 10**9
p = ""
for i in range(len(perm)):
    temp = 0
    a = ""
    for j in range(n):
        if s[j] != perm[i][j % 3]:
            temp += 1
            a += perm[i][j % 3]
        else:
            a += s[j]
    if temp < ans:
        ans = temp
        p = a
print(ans)
print(p)
