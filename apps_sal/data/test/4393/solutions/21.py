n = int(input())
a = input()
c = 1
i = 0
s = []
while i < n:
    s.append(a[i])
    i += c
    c += 1
print(*s, sep="")
