n = int(input())
line = [0]
for i in range(n):
    line.append(int(input()))
check = [0 for i in range(n + 1)]
count = 0
check[1] = 1
a = 1
while True:
    count += 1
    if line[a] == 2:
        break
    else:
        a = line[a]
        check[a] += 1
    if check[a] > 1:
        count = -1
        break
print(count)
