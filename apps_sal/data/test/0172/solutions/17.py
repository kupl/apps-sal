from sys import stdin, stdout
n = int(stdin.readline())
first = list(map(int, stdin.readline().split()))
second = list(map(int, stdin.readline().split()))
cntf = [0, 0, 0, 0, 0]
cnts = [0, 0, 0, 0, 0]
for i in range(n):
    cntf[first[i] - 1] += 1
    cnts[second[i] - 1] += 1
label = 1
for i in range(5):
    if (cntf[i] + cnts[i]) % 2:
        label = 0
if not label:
    stdout.write('-1')
else:
    ans = 0
    for i in range(5):
        m = (cntf[i] + cnts[i]) // 2
        ans += max(cntf[i] - m, 0)
    stdout.write(str(ans))
