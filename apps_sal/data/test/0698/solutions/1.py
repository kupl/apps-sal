(x, k) = map(int, input().split())
a = [1] * x
for i in range(k):
    s = input().split()
    if s[0] == '1':
        a[int(s[1])] = 0
        a[int(s[2])] = 0
    else:
        a[int(s[1])] = 0
i = 1
t = 0
while i < x:
    if a[i] == 1:
        if i + 1 < x and a[i + 1] == 1:
            t += 1
        i += 2
    else:
        i += 1
print(sum(a[1:]) - t, sum(a[1:]))
