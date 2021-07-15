def all_true(stars, n, m):
    for i in range(n):
        for j in range(m):
            if not stars[i][j]:
                return False
    return True

def get_biggest_star(ar, i, j):
    ans = 0
    cur = i - 1
    while cur >= 0 and ar[cur][j] == '*':
        ans += 1
        cur -= 1

    length = 0
    cur = i + 1
    while cur < n and ar[cur][j] == '*':
        length += 1
        cur += 1
    ans = min(ans, length)

    length = 0
    cur = j - 1
    while cur >= 0 and ar[i][cur] == '*':
        length += 1
        cur -= 1
    ans = min(ans, length)

    length = 0
    cur = j + 1
    while cur < m and ar[i][cur] == '*':
        length += 1
        cur += 1
    ans = min(ans, length)

    return ans

n, m = list(map(int, input().split()))

ar = []

stars = []

for i in range(n):
    cur = input()
    st = []
    for i in range(m):
        if cur[i] == '.': st.append(True)
        else: st.append(False)
    stars.append(st)
    ar.append(cur)

finalAns = []
ans = 0
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if ar[i][j] == '.': continue
        length = get_biggest_star(ar, i, j)
        if length > 0:
            ans += 1
            finalAns.append([i+1, j+1, length])
            stars[i][j] = True
            temp = 0
            while temp < length:
                temp += 1
                stars[i-temp][j] = True
            temp = 0
            while temp < length:
                temp += 1
                stars[i+temp][j] = True
            temp = 0
            while temp < length:
                temp += 1
                stars[i][j-temp] = True
            temp = 0
            while temp < length:
                temp += 1
                stars[i][j+temp] = True

##print(*stars, sep = '\n')

if all_true(stars, n, m):
    print(ans)
    for i in finalAns:
        print(*i)
else:
    print(-1)
            

