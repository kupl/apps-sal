n = int(input())
a = list(map(int, input().split()))
s = 0
for i in range(len(a)):
    s += a[i]
e = s // n
while len(a) != 0:
    u = e - a[0]
    print(a[0], u)
    a.pop(0)
    a.remove(u)
