n = int(input())
v = list(map(int, input().split()))

first = {}
second = {}

for i in range(n):
    if i % 2 == 0:
        if v[i] in first:
            first[v[i]] += 1
        else:
            first[v[i]] = 1
    else:
        if v[i] in second:
            second[v[i]] += 1
        else:
            second[v[i]] = 1

first = sorted(first.items(), key=lambda x: x[1])
second = sorted(second.items(), key=lambda x: x[1])

f = first.pop()
s = second.pop()

if f[0] == s[0]:
    if len(first) >= 1:
        if len(second) >= 1:
            f2 = first.pop()
            s2 = second.pop()

            if f2[1] + s[1] > f[1] + s2[1]:
                f = f2
            else:
                s = s2
        else:
            s = second.pop()
    elif len(second) >= 1:
        f = first.pop()
    else:
        s = (0, 0)

print(n - f[1] - s[1])
