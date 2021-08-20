s = input()
ar = s.split()
n = int(ar[0])
m = int(ar[1])
a = []
b = []
s = input()
for i in s.split():
    a += [int(i)]
s = input()
for i in s.split():
    b += [int(i)]
if max(min(a) * 2, max(a)) < min(b):
    print(max(min(a) * 2, max(a)))
else:
    print(-1)
