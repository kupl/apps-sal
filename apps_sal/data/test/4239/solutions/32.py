n = int(input())

ans = [-1] * (n + 1)

ans[0] = 0
for i in range(1, n + 1):
    num = i
    data = ans[i - 1] + 1
    for j in range(8):
        index = i - 6**j
        if index < 0:
            break
        data = min(data, ans[index] + 1)
    for j in range(8):
        index = i - 9**j
        if index < 0:
            break
        data = min(data, ans[index] + 1)
    ans[i] = data
print((ans[-1]))
