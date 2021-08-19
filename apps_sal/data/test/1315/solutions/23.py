n = int(input())
line = list(map(int, input().split()))
for i in range(n):
    line[i] += i
line.sort()
is_happy = True
for i in range(1, n):
    if line[i] == line[i - 1]:
        is_happy = False
        break
if is_happy:
    print(' '.join([str(line[i] - i) for i in range(n)]))
else:
    print(':(')
