n, v = [int(i) for i in input().split()]
s = []
for i in range(n):
    s.append([min([int(i) for i in input().split()][1:]), i])
a = []
s.sort()
for i in range(len(s)):
    if v > s[i][0]:
        a.append(s[i][1])
print(len(a))
a.sort()
print(" ".join([str(i + 1) for i in a]))
