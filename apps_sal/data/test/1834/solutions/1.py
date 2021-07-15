n = int(input())
m = list(map(int, input().split()))
a = []
m.sort()
i = 0
j = len(m) - 1
while len(m) != len(a):
    if len(a) % 2 != 0:
        a.append(m[j])
        j -= 1
    else:
        a.append(m[i])
        i += 1
print(*a)
