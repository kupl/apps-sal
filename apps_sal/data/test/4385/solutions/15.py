a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = int(input())
l = []
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
ans = 0
for i in range(5):
    for j in range(i + 1, 5):
        if l[j] - l[i] > k:
            ans += 1
if ans == 0:
    print('Yay!')
else:
    print(':(')
