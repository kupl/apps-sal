from collections import deque
n = int(input())
a = list(map(int, input().split()))
b = deque()
reverse = 1
for i in range(n):
    if reverse == 1:
        b.append(a[i])
        reverse *= -1
    else:
        b.appendleft(a[i])
        reverse *= -1
b_list = list(b)
if reverse == 1:
    print(*b_list)
else:
    print(*b_list[::-1])
