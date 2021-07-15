n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = set()
t = 0
i = 0
for j in range(n):
    if b[j] in s:
        print(0, end=' ')
    else:
        while a[i] != b[j]:
            s.add(a[i])
            t += 1
            i += 1
        t += 1
        s.add(a[i])
        i += 1
        print(t, end=' ')
        t = 0

