n = int(input())
s = input()
x = []
x2 = []
y = []
y2 = []
z = []
z2 = []
a = 0
while a<n:
    if a% 3 == 0:
        x.append("G")
    elif a%3 == 1:
        x.append("B")
    else:
        x.append("R")
    a += 1
a = 0
while a<n:
    if a% 3 == 0:
        x2.append("G")
    elif a%3 == 1:
        x2.append("R")
    else:
        x2.append("B")
    a += 1
a = 0
while a<n:
    if a% 3 == 0:
        y.append("B")
    elif a%3 == 1:
        y.append("G")
    else:
        y.append("R")
    a += 1
a = 0
while a<n:
    if a% 3 == 0:
        y2.append("B")
    elif a%3 == 1:
        y2.append("R")
    else:
        y2.append("G")
    a += 1
a = 0
while a<n:
    if a% 3 == 0:
        z.append("R")
    elif a%3 == 1:
        z.append("G")
    else:
        z.append("B")
    a += 1
a = 0
while a<n:
    if a% 3 == 0:
        z2.append("R")
    elif a%3 == 1:
        z2.append("B")
    else:
        z2.append("G")
    a += 1
ans = float("inf")
dore = [x,x2,y,y2,z,z2]
d = 0
tmp = 0
for i in range(n):
    if x[i] != s[i]:
        tmp += 1
if tmp < ans:
    d = 0
    ans = tmp
tmp = 0
for i in range(n):
    if x2[i] != s[i]:
        tmp += 1
if tmp < ans:
    d = 1
    ans = tmp

tmp = 0
for i in range(n):
    if y[i] != s[i]:
        tmp += 1
if tmp < ans:
    d = 2
    ans = tmp
tmp = 0
for i in range(n):
    if y2[i] != s[i]:
        tmp += 1
if tmp < ans:
    d = 3
    ans = tmp

tmp = 0
for i in range(n):
    if z[i] != s[i]:
        tmp += 1
if tmp < ans:
    d = 4
    ans = tmp
tmp = 0
for i in range(n):
    if z2[i] != s[i]:
        tmp += 1
if tmp < ans:
    d = 5
    ans = tmp
print(ans)
print("".join(dore[d]))
