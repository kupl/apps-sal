n = int(input())
a = list(map(int, input().split()))
s = set()
last = 0
for i in range(len(a) - 1, -1, -1):
    if not a[i] in s:
        last = a[i]
        s.add(a[i])
print(last)
