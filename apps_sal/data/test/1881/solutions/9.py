n, k = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
ans = [-1] * (max(p) + 1)
ans[0] = 0
for i in range(n):
    if ans[p[i]] < 0:
        position = p[i] - k + 1
        for j in range(max(0, p[i] - k + 1), p[i] + 1):
            if ans[j] < 0:
                position = j
                break
        j = max(0, position - 1)
        key = ans[j]
        count = 0
        while j >= 0:
            if ans[j] != key:
                position1 = j + 1
                break
            j -= 1
            count += 1
        if count + p[i] + 1 - position > k:
            key = position
        for j in range(position, p[i] + 1):
            ans[j] = key

for i in range(n):
    if i != len(p) - 1:
        wk1 = " "
    else:
        wk1 = "\n"
    print(ans[p[i]], end=wk1)
