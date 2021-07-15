n = int(input())
a = list(map(int, input().split()))
x = max(a)
s = set()
i = 0
while i < len(a):
    if x % a[i] == 0:
        t = len(s)
        s.add(a[i])
        if len(s) > t:
            a.pop(i)
        else:
            i += 1
    else:
        i += 1
print(x, max(a))
