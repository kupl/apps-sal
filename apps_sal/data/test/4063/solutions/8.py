n = int(input())
d = list(map(int, input().split()))
d.sort()

s = int(len(d) / 2)

if d[s] != d[s - 1]:
    print(d[s] - d[s - 1])
elif d[s] == d[s - 1]:
    print(0)
