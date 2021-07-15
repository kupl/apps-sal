n = int(input())
ns = list(map(int, input().split()))[::-1]
fs = []

for x in ns:
    if x not in fs:
        fs.append(x)

print(len(fs))
print(*fs[::-1])
