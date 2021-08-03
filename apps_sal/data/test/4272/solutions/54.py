n = int(input())
ss = input()
cnt = 0
for i in range(len(ss) - 2):
    if ss[i] == 'A' and ss[i + 1] == 'B' and ss[i + 2] == 'C':
        cnt += 1
print(cnt)
