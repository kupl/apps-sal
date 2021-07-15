from collections import deque
k = int(input())
a = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(k-1):
    b = a.popleft()
    if b%10 != 0: a.append(b*10+b%10-1)
    a.append(b*10+b%10)
    if b%10 != 9: a.append(b*10+b%10+1)
print(a[0])
