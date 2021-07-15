n, k = map(int, input().split())
list01 = input().split()
list02 = [int(a) for a in list01]
x = 0
for i in list02:
    if i >= k:
        x += 1
    else:
        pass
print(x)
