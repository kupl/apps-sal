n = int(input())
a = []
b = []
for _ in range(n):
    c = list(map(int, input().split()))
    a.append(c[0])
    b.append(c[1])
d = list(zip(b, a))
d.sort()
# print(d)

time = 0
for i in range(n):
    time += d[i][1]
    if d[i][0] < time:
        print("No")
        return
print("Yes")
