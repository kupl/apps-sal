moji = str(input())
N = len(moji)
FM = moji[:N // 2]
if N % 2 == 0:
    LM = moji[-1:N // 2 - 1:-1]
else:
    LM = moji[-1:N // 2:-1]
ct = 0
for i in range(N // 2):
    if FM[i] != LM[i]:
        ct += 1
print(ct)
