s = input()
k = int(input())
l = tuple(map(int, input().split()))

r = 0

p = 1
for i in s:
    r+=l[ord(i)-97]*p
    p += 1

z = max(l)

for i in range(k):
    r += z*p
    p += 1
print(r)

