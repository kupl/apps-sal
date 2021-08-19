N = int(input())
c = list(input())
w = 0
r = N - 1
ans = 0
while w < r:
    for i in range(w, r):
        if c[i] == 'W':
            c[i] = 'R'
            w = i
            break
    else:
        break
    for j in range(r, w, -1):
        if c[j] == 'R':
            c[j] = 'W'
            r = j
            break
    else:
        break
    ans += 1
print(ans)
