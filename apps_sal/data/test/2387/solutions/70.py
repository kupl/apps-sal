def kakko(S):
    cum = 0
    mi = 0
    for s in S:
        cum += 1 if s == '(' else -1
        mi = min(mi, cum)
    return (-mi, cum - mi)

N = int(input())
S = [kakko(input()) for _ in range(N)]

plus = []
minus = []

for l, r in S:
    if l <= r:
        plus.append((l, r))
    else:
        minus.append((l, r))

plus.sort(key=lambda a: a[0])
minus.sort(key=lambda a: a[1], reverse=True)
M = 0
for l, r in (plus + minus):
    M -= l
    if M < 0:
        print('No')
        return
    M += r

print(('Yes' if M == 0 else 'No'))

