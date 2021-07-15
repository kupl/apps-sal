n = int(input())
a = list(map(int, input().split()))
b = []
cur = 0
while cur < n:
    cnt = 0
    size = 0
    while cur < n and cnt < 3:
        if a[cur] < 0:
            cnt += 1
        cur += 1
        size += 1
    if cnt == 3:
        cur -= 1
        size -= 1
    b.append(size)

print(len(b))
print(" ".join(map(str, b)))
