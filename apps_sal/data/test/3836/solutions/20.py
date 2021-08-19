from collections import defaultdict
N = int(input())
num = 0
cnt = 0
rec = defaultdict(list)
cnt10 = 0
cnt01 = 0
for i in range(N):
    (a, b) = input().split()
    if a == '11':
        num += int(b)
        cnt += 1
    elif a == '01':
        cnt01 += 1
        rec[a].append(int(b))
    elif a == '10':
        cnt10 += 1
        rec[a].append(int(b))
    else:
        rec[a].append(int(b))
rec['10'] = sorted(rec['10'])
rec['01'] = sorted(rec['01'])
for i in range(min(cnt10, cnt01)):
    num += rec['10'].pop()
    num += rec['01'].pop()
q = rec['10'] + rec['01'] + rec['00']
q = sorted(q, reverse=True)
num += sum(q[:cnt])
print(num)
