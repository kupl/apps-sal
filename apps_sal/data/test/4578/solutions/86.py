n, x = map(int, input().split())
m = []
for i in range(n):
    m.append(int(input()))
    x -= m[i]

counter = len(m)
while(1):
    if x < 0:
        print(counter - 1)
        break
    else:
        x -= min(m)
        counter += 1
