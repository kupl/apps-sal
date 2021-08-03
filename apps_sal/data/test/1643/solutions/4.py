s = [int(x) for x in list(input())]
n = len(s)
b = [0] * n
counter = 0
for i in range(n - 1, -1, -1):
    if s[i] == 0:
        counter += 1
    elif counter > 0:
        counter -= 1
    else:
        s[i] = 0
arr = ''
for item in s:
    arr += str(item)
print(arr)
