n, m = list(map(int, input().split()))
arr = [int(i) for i in input().split()]
res, s = 0, ""
for i in range(m):
    b = [int(x) for x in input().split()]
    if b[0] == 1:
        arr[b[1] - 1] = b[2] - res
    elif b[0] == 2:
        res += b[1]
    else:
        s += str(arr[b[1] - 1] + res) + '\n'
print(s)

