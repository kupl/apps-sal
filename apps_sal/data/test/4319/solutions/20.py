n = int(input())
stairs = list(map(int, input().split(" ")))

lengths = []
last = 0
for i in stairs:
    if i != last + 1:
        lengths.append(last)
    last = i

lengths.append(last)
print(len(lengths))
print(*lengths)


