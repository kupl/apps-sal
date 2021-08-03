n = int(input())
s = input().split()
cl = []
for i in range(n):
    if s[i] not in cl and s[i] != '0':
        cl.append(s[i])

print(len(cl))
