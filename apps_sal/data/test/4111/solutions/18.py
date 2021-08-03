n = int(input())
l = list(map(int, input().split()))
s1 = 0
s2 = 0
for i in range(1, n, 2):
    s1 += l[i]
for i in range(2, n, 2):
    s2 += l[i]
count = 0
if s1 == s2:
    count += 1
for i in range(1, n):
    if i % 2:
        s1 -= l[i]
        s1 += l[i - 1]
    else:
        s2 -= l[i]
        s2 += l[i - 1]
    if s1 == s2:
        count += 1
print(count)
