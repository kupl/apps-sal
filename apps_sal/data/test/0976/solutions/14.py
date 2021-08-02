listx = []

x, y = map(int, input().split(' '))
for i in range(x):
    a, b = map(int, input().split(' '))
    listx.append([a, b])

time = 1
curr = 0
mins = 0
while curr < x:
    while time + y <= listx[curr][0]:
        time += y
    mins += listx[curr][1] - time + 1
    time = listx[curr][1]
    curr += 1
    time += 1
print(mins)
