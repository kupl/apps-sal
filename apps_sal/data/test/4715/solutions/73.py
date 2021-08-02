data = list(input().split())
s = 1
for i in range(1, len(data)):
    for j in range(0, i):
        if data[i] == data[j]:
            data[i] = -1
    if data[i] != -1:
        s = s + 1
print(s)
