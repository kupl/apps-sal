N = int(input())
A = list(map(int, input().split()))
cnt_odd = 0
cnt_4 = 0
for a in A:
    if a % 2 != 0:
        cnt_odd += 1
    elif a % 4 == 0:
        cnt_4 += 1
if cnt_odd + cnt_4 == N and cnt_odd - 1 == cnt_4:
    print('Yes')
else:
    print(('Yes' if cnt_4 >= cnt_odd else 'No'))
