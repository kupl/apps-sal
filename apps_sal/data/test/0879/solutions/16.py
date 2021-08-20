n = int(input())
arr = list(map(int, input().split()))
c = n
path = [n]
while c != 1:
    c = arr[c - 2]
    path.append(c)
path = path[::-1]
print(*path)
