(x, n) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort()
result = x
for i in range(100):
    if x in l:
        pass
    else:
        result = x
        break
    if x - i in l:
        pass
    elif x - i >= 0:
        result = x - i
        break
    if x + i in l:
        pass
    elif x + i <= 101:
        result = x + i
        break
print(result)
