n = input("")

(n, t, c) = n.split(" ")

line = input("")
line = line.split(" ")
line.append("1000000001")
ans = 0
start = 0
current = 0
for x in range(len(line)):
    if int(line[x]) > int(t):
        ans += max(0, x - start + 1 - int(c))
        start = x + 1


print(ans)
