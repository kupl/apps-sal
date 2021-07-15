r, c = list(map(int, input().split()))

rt = [0] * 10
ct = [0] * 10

for i in range(r):
    s = str(input())
    for j in range(len(s)):
        if s[j] == 'S':
            rt[i] = 1
            ct[j] = 1

cnt = 0
for i in range(r):
    for j in range(c):
        if rt[i] == 0 or ct[j] == 0:
            cnt += 1

print(cnt)

