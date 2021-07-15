input()
a = list(map(int,input().split()))
a.sort()
s = 0
for i in enumerate(a, 2):
    s += i[0] * i[1]
print(s - a[-1])
