def inpmap():
    return list(map(int, input().split()))
n, a, b = inpmap()
arr = list(input())
s = 0 if a > b else 1
ix = [a, b]
res = 0
for i in range(n):
    if arr[i] == '.':
        if ix[s] > 0:
            ix[s] -= 1
            res += 1
        s = 1 - s
    else:
        s = 0 if ix[0] > ix[1] else 1
print(res)

