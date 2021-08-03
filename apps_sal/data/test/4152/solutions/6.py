n = int(input())
L = list(map(int, input().split()))
s = set(L)
ss = s.copy()
dic = dict()
for i in L:
    dic[i] = 0
for i in L:
    dic[i] += 1

for i in s.copy():
    for j in range(32):
        t = 1 << j
        if t - i in s:
            if i != t - i:
                ss -= {t - i, i}
            elif dic[i] != 1:
                ss -= {i}

ans = 0
for i in ss:
    ans += dic[i]

print(ans)
