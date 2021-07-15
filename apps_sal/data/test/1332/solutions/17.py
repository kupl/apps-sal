A = input().split()
x = 5
s = 0
for i in range(5):
    s += int(A[i])

if (s % x == 0) and (s != 0):
    print(str(s // x))
else:
    print('-1')


