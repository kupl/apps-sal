n = int(input())
s = input()
a = list(map(int, input().split()))
maxl = -1
mini = 100000000000000000000000
for i in range(n):
    if s[i] == 'R':
        maxl = a[i]
    if s[i] == 'L' and maxl != -1:
        mini = min(mini, a[i] - maxl)
if mini == 100000000000000000000000:
    print(-1)
else:
    print(mini // 2)
