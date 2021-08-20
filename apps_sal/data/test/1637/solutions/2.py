import sys
input = sys.stdin.readline
(n, m) = [int(x) for x in input().split()]
s = sys.stdin.read()
j = 0
inp = []
numb = 0
if s[j] == '-':
    sign = -1
    j += 1
else:
    sign = 1
while j < len(s) - 1:
    numb = 10 * numb + ord(s[j]) - 48
    j += 1
    if s[j] < '-':
        inp.append(sign * numb)
        j += 1
        if j < len(s) and s[j] == '-':
            sign = -1
            j += 1
        else:
            sign = 1
        numb = 0
if j == len(s) - 1:
    numb = 10 * numb + ord(s[j]) - 48
    inp.append(sign * numb)
order = sorted(range(n), key=lambda i: inp[2 * i] - inp[2 * i + 1])
score = [0] * n
val = sum(inp[1:2 * n:2])
for ind in range(n):
    i = order[ind]
    score[i] += val + inp[2 * i + 1] * (ind - 1) + inp[2 * i] * (n - ind - 1)
    val += inp[2 * i] - inp[2 * i + 1]
for _ in range(m):
    u = inp[2 * n + 2 * _] - 1
    v = inp[2 * n + 2 * _ + 1] - 1
    s = min(inp[2 * u] + inp[2 * v + 1], inp[2 * v] + inp[2 * u + 1])
    score[u] -= s
    score[v] -= s
sys.stdout.write(' '.join((str(x) for x in score)))
