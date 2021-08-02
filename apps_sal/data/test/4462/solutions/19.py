from collections import deque

n = int(input())
A = list(map(int, input().split()))

cnt_2 = 0
cnt_4 = 0
for i in range(n):
    a = A[i]
    if a % 4 == 0:
        cnt_4 += 1
    elif a % 2 == 0:
        cnt_2 += 1
cnt_else = n - cnt_2 - cnt_4
cnt_else += cnt_2 % 2

if cnt_else - 1 <= cnt_4:
    print("Yes")
else:
    print("No")
