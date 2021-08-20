(n, a, b, k) = [int(i) for i in input().split()]
s = input()
l = []
i = 0
j = 0
while i < len(s):
    if s[i] == '1':
        j = 0
    else:
        j += 1
        if j % b == 0:
            l += [i + 1]
            j = 0
    i += 1
l = l[a - 1:]
print(len(l))
print(*l)
