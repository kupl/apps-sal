line = input().split()
n = int(line[0])
t = int(line[1])

line = input().split()
arr = [int(num) for num in line]
n = 0
while n < t - 1:
    n += arr[n]

if n == t - 1:
    print('YES')
else:
    print('NO')
