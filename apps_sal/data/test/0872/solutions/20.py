n = int(input())
l = list(map(int, input().split()))
cnt1 = 0
cnt2 = 0
for i in range(n):
    if l[i] % 2 == 0:
        cnt1 = 1
    else:
        cnt2 = 1
if (cnt1 and cnt2):
    print(' '.join(map(str, sorted(l))))
else:
    print(' '.join(map(str,l)))

