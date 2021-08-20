N = int(input())
A = list(map(int, input().split()))
next_number = 1
cnt = 0
for a in A:
    if a == next_number:
        next_number += 1
    else:
        cnt += 1
if cnt == len(A):
    print('-1')
else:
    print(cnt)
