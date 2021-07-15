n = int(input())
s, t = input().split()

lists = []
for i in range(n):
    lists.append(s[i])
    lists.append(t[i])

print("".join(lists))
