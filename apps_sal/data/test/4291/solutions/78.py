n, q = list(map(int, input().split()))
s = input()
lr = [list(map(int, input().split())) for i in range(q)]

rui = [0] * (n + 1)
tmp = 0
for i in range(n):
    if s[i - 1] == 'A' and s[i] == 'C':
        tmp += 1
    rui[i] = tmp

for l, r in lr:
    print((rui[r - 1] - rui[l - 1]))
