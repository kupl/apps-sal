n = int(input())
b = [(int(x), y) for x, y in zip(input().split(), list(range(n)))]
b.sort()
b += [(0, 0)]
t = 0
ans = []
i = 0
seq = 0
while i < n:
    while b[i][0] != b[i + 1][0]:
        ans.append(str(b[i][0]) + " 0")
        i += 1
        if i == n:
            break
    if i == n:
        i += 1
    elif b[i][0] == b[i + 1][0]:
        seq = 0
        while b[i][0] == b[i + 1][0]:
            if seq == 0:
                seq = b[i + 1][1] - b[i][1]
                i += 1
            elif b[i + 1][1] - b[i][1] == seq:
                i += 1
            else:
                seq = -1
                i += 1
        if seq == -1:
            i += 1
        else:
            ans.append(str(b[i][0]) + " " + str(seq))
            i += 1


print(len(ans))
print("\n".join(ans))
