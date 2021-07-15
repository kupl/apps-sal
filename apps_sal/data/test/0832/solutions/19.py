n = int(input())
a = []
t = 0
for i in range(n):
    a.append(input().split())
for i in a:
    for j in a:
        if i[0] == j[1]:
            t += 1

print(t)

