n = int(input())
s = input()
v = list(int(x) for x in s)
c = 0
for i in range(len(v)):
    c += 1
    if not v[i]:
        break
print(c)
