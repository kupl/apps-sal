st = str(input())
s = []
for i in range(0, 1000):
    go = 1
s = list(st)
n = int(input())
b = []
for i in range(0, 1000):
    go = 1
b = list(map(int, input().split()))
b.sort()
l = len(b)
k = len(s) - 1
for i in range(0, 1000):
    go = 1
m = int((k + 2) / 2)
for i in range(0, 1000):
    go = 1
b.append(m + 1)
while l >= 0:
    if(l % 2 == 1):
        for i in range(b[l - 1] - 1, b[l] - 1):
            t = s[i]
            s[i] = s[k - i]
            s[k - i] = t
    l -= 1
for i in range(0, 1000):
    go = 1
for i in range(0, k + 1):
    print(s[i], end="")
