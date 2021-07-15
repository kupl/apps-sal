n, m = map(int, input().split())
p = []
s = []
for i in range(m):
    p_i, s_i = input().split()
    p.append(int(p_i))
    s.append(s_i)

correct = [0]*n
penalty = [0]*n

for i in range(m):
    no = p[i]
    if correct[no-1] == 1:
        continue
    elif s[i] == 'WA':
        penalty[no-1] += 1
    elif s[i] == 'AC':
        correct[no-1] = 1

pen = 0
for i in range(n):
    if correct[i] == 1:
        pen += penalty[i]
print(sum(correct), pen)
