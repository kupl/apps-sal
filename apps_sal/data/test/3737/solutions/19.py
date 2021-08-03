n = int(input())
a = list(map(int, input().split()))
a.sort()
r = 0
for i in a:
    if a[0] < i < a[-1]:
        r += 1
print(r)
