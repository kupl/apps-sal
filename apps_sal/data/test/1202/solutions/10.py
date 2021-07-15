a = int(input())
pol1 = []
pol2 = []
for i in range(a):
    x, y = map(int, input().split())
    pol1.append(x)
    pol2.append(y)
f = 0
s = 0
ans1 = [0] * a
ans2 = [0] * a
count = 0
while True:
    count += 1
    if pol1[f] < pol2[s]:
        ans1[f] = 1
        f += 1
    else:
        ans2[s] = 1
        s += 1
    if count == a:
        break
for i in range(a // 2):
    ans1[i] = 1
    ans2[i] = 1
s = ''
for i in ans1:
    s += str(i)
print(s)
s = ''
for i in ans2:
    s += str(i)
print(s)
