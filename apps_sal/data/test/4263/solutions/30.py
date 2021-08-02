s = input()
ls = len(s)

cnt = 0
ma = 0
for i in range(ls):
    if(s[i] in 'ACGT'):
        cnt += 1
    else:
        ma = max(ma, cnt)
        cnt = 0

ma = max(ma, cnt)
print(ma)
