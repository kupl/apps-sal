n = int(input())
words = list(input().split())
volumes = []
for x in words:
    a = 0
    for y in x:
        if y.upper() == y:
            a += 1
    volumes.append(a)
print(max(volumes))
