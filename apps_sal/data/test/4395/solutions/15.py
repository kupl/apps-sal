n = int(input())
s = input()
mask = ['RGB', 'RBG', 'BRG', 'BGR', 'GBR', 'GRB']
ans = 10000000000
anss = ''
for i in range(6):
    k = n // 3
    ss = mask[i] * k + mask[i][:n % 3]
    now = 0
    for j in range(n):
        if s[j] != ss[j]:
            now += 1
    if now < ans:
        ans = now
        anss = ss

print(ans)
print(anss)
    

