N = int(input())

t = [0]
x = [0]
y = [0]
for i in range(N):
    l = [int(c) for c in input().split()]
    t.append(l[0])
    x.append(l[1])
    y.append(l[2])

for i in range(N):
    move = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    time = t[i+1]-t[i]
    if time%2 ^ move%2 == 1 or time < move:
        print("No")
        return

print("Yes")
