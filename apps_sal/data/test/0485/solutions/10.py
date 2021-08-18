n = int(input())
l = []
for i in range(4 * n + 1):
    a, b = list(map(int, input().split()))
    l.append([a, b])
x1 = -1
x2 = -1
y1 = -1
y2 = -1
h = [0] * 51
for i in range(4 * n + 1):
    h[l[i][0]] += 1
for i in range(51):
    if(h[i] >= n and x1 == -1):
        x1 = i
    if(h[50 - i] >= n and x2 == -1):
        x2 = 50 - i
h = [0] * 51
for i in range(4 * n + 1):
    h[l[i][1]] += 1
for i in range(51):
    if(h[i] >= n and y1 == -1):
        y1 = i
    if(h[50 - i] >= n and y2 == -1):
        y2 = 50 - i
for i in range(4 * n + 1):
    if(l[i][0] == x1 or l[i][0] == x2):
        if(not(l[i][1] >= y1 and l[i][1] <= y2)):
            print(l[i][0], l[i][1])
            break
    else:
        if(l[i][1] == y1 or l[i][1] == y2):
            if(not(l[i][0] >= x1 and l[i][0] <= x2)):
                print(l[i][0], l[i][1])
                break
        else:
            print(l[i][0], l[i][1])
            break
