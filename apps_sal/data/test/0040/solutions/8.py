n = int(input())
a = [0] * n
b = [0] * n
s1 = True
s2 = True
for i in range(n):
    (a[i], b[i]) = list(map(int, input().split()))
    if a[i] != b[i]:
        s1 = False
if a == list(reversed(sorted(a))):
    s2 = False
if not s1:
    print('rated')
elif not s2:
    print('maybe')
else:
    print('unrated')
