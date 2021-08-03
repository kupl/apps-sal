n = int(input())
s = []
for i in range(n):
    s.append(int(input()))
x = 0
t = []
for i in range(n):
    if s[i] % 10 == 0:
        t.append(i)
        x += s[i]
cnt = 0
for i in t:
    del s[i - cnt]
    cnt += 1
s.sort()
while sum(s) % 10 == 0 and len(s) > 0:
    del s[0]
if sum(s) == 0:
    print(0)
else:
    print(sum(s) + x)
