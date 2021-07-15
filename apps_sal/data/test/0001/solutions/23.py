a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for length in range(2, 30):
    for first in range(1, 10):
        for pos in range(1, length):
            a.append(int(str(first) + '9' * (pos - 1) + '8' + '9' * (length - pos - 1)))
        a.append(int(str(first) + '9' * (length - 1)))
    
n = int(input())
l = 0
r = len(a)
while l < r - 1:
    middle = (l + r) // 2
    if (a[middle] <= n):
        l = middle
    else:
        r = middle
        
print(a[l])
