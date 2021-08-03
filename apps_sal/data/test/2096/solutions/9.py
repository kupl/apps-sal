from collections import defaultdict as defdict

n = int(input())

d = defdict(int)
a = list(map(int, input().split()))

for i in a:
    d[i] += 1

b = set(i for i in a if d[i] > 1)
c = [i for i in a if d[i] == 1]

##print('b =', b)

mx = len(b) + (len(c) // 2)

d = defdict(int)
answ = [None] * (n * 2)

cnt_diff_1 = 0
cnt_diff_2 = 0

for i, x in enumerate(a):
    if cnt_diff_1 < mx:
        if x in b:
            if d[x] == 0:
                answ[i] = '1'
                d[x] += 1
                cnt_diff_1 += 1

for i, x in enumerate(a):
    if cnt_diff_1 < mx:
        if x not in b:
            answ[i] = '1'
            cnt_diff_1 += 1

# print(d)
cnt1 = cnt_diff_1
cnt2 = 0

# print(cnt_diff_1)
# print(answ)
# print(mx)

for i, x in enumerate(a):
    if answ[i] == '1':
        continue
    if x in b:
        if d[x] == 0:
            answ[i] = '2'
            d[x] = 2
            cnt_diff_2 += 1
            cnt2 += 1
        elif d[x] == 1:
            answ[i] = '2'
            d[x] += 1
            cnt_diff_2 += 1
            cnt2 += 1
        else:
            if cnt1 < n:
                answ[i] = '1'
                cnt1 += 1
            else:
                answ[i] = '2'
                cnt2 += 1
    else:
        if cnt2 < n:
            answ[i] = '2'
            cnt2 += 1
            cnt_diff_2 += 1
        else:
            answ[i] = '1'
            cnt1 += 1
##            print('cnt2 =', cnt2)
# print(cnt_diff_2)
##            print('cnt1 =', cnt1)
            cnt_diff_1 += 1

##print(cnt_diff_1, cnt_diff_2)
# print()

##cnt1 = len(set(a[i] for i in range(2 * n) if answ[i] == '1'))
##cnt2 = len(set(a[i] for i in range(2 * n) if answ[i] == '2'))
##print(cnt1, cnt2)
print(cnt_diff_1 * cnt_diff_2)
print(' '.join(answ))
