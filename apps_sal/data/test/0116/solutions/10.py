i = input().split()
start = max(int(i[0]), int(i[2]))
end = min(int(i[1]), int(i[3]))
res = end - start + 1
if start <= int(i[4]) <= end:
    res -= 1
if res < 0:
    res = 0
print(res)
