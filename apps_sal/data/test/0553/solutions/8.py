n = int(input())
arr = []
for i in range(n):
    line = int(input())
    arr.append(line)
m = 6
for i in range(n):
    for j in range(i + 1, n):
        t1 = arr[i]
        t2 = arr[j]
        tm = 0
        for k in range(6):
            if t1 % 10 != t2 % 10:
                tm += 1
            t1 //= 10
            t2 //= 10
        if tm < m:
            m = tm
if m % 2 == 0:
    m -= 1
m //= 2
if m < 0:
    m = 0
if n == 1:
    m = 6
print(m)
