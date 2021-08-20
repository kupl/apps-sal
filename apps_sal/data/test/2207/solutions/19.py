(n, m) = list(map(int, input().split()))
c = []
for i in range(n):
    a = list(input())
l = 0
for i in range(len(a) - 1):
    if a[i] == 'B' and a[i + 1] == '.':
        l += 1
if a[-1] == 'B':
    l += 1
print(l)
