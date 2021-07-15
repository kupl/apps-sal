N = int(input())
A = list(map(int, input().split()))
a = 0
#
for i in range(0, N):
    if A[i] % 2 == 0:
        if A[i] % 3 == 0 or A[i] % 5 == 0:
            a += 1
    else:
        a += 1
# 条件を満たした書類が　N の数と同じになった場合
if N == a:
    print("APPROVED")
else:
    print('DENIED')
