n = int(input())
h = list(map(int, input().split()))
h.append(0)
count = 0
while h != [0] * (n + 1):
    for i in range(len(h)):
        if h[i] != 0:
            break
    for j in range(i, len(h) + 1):
        if h[j] == 0:
            break
    for x in range(i, j):
        h[x] -= 1
    count += 1
print(count)
