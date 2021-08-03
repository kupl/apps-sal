n = int(input())
s = [int(i) for i in input().split()]

t = 0
l = "0"
a = []

for i in range(len(s)):
    if(s[i] == 1 and i > 0):
        t += 1
        a.append(l)
    l = str(s[i])

t += 1
a.append(l)

print(t)
print(" ".join(a))
