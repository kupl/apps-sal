n = int(input())
say = []
for i in range(n):
    qq = []
    for i in range(int(input())):
        qq.append(list(map(int, input().split())))
    say.append(qq)
ans = 0
for bit in range(1 << n):
    plate = 0
    L = [(bit >> i) & 1 for i in range(n)]
    for i in range(n):
        if L[i] == 0: continue
        for l in say[i]:
            if L[l[0] - 1] != l[1]:
                plate = 1; break
        if plate: break
    else:
        ans = max(ans, sum(L))
print(ans)
