n = int(input())
parent = [*map(int, input().split())]
l = [n]
while l[-1] != 1:
    l.append(parent[l[-1] - 2])
print(' '.join(map(str, l[::-1])))
