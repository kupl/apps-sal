n, t = list(map(int, input().split()))
data = list(map(int, input().split()))
s = 0
new = []
for i in data:
    s += (86400 - i)
    new.append(s)
for i in range(n):
    if new[i] >= t:
        print(i + 1)
        break
else:
    print(n)
