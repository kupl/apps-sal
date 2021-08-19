s = input().rstrip().split(' ')
(n, c) = (int(s[0]), int(s[1]))
x = input().rstrip().split(' ')
max = int(x[0]) - int(x[1]) - c
for i in range(1, n - 1):
    if int(x[i]) - int(x[i + 1]) - c > max:
        max = int(x[i]) - int(x[i + 1]) - c
if max < 0:
    max = 0
print(max)
