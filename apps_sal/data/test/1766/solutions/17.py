(n, t) = (int(input()), list(map(int, input().split())))
(s, i, j) = ([0, 0], 0, n - 1)
for k in range(n):
    if t[i] < t[j]:
        s[k % 2] += t[j]
        j -= 1
    else:
        s[k % 2] += t[i]
        i += 1
print(s[0], s[1])
