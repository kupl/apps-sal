n, q = list(map(int, input().split()))
s = input()
lr = [list(map(int, input().split())) for i in range(q)]

rui = [0] * (n + 1)
tmp = 0
for i in range(len(s)):
    if s[i - 1] == 'A' and s[i] == 'C':
        tmp += 1
    rui[i] = tmp

for i in range(q):
    print((rui[lr[i][1] - 1] - rui[lr[i][0] - 1]))
