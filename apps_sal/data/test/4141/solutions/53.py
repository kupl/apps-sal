# 入力
N = int(input())
A = list(map(int, input().split()))

gusu = 0
cnt = 0
# リストの中の偶数を調べる
for i in range(N):
    if A[i] % 2 == 0:
        gusu += 1

# 3 or 5で割り切れるか調べる
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            cnt += 1

if gusu == cnt:
    print('APPROVED')
else:
    print('DENIED')
