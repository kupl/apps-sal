(n, m) = map(int, input().split())
st = []
cp = []
for i in range(n):
    st.append(list(map(int, input().split())))
for i in range(m):
    cp.append(list(map(int, input().split())))
for i in range(n):
    distance = 0
    shortest_cp = 0
    for j in range(m):
        if j == 0:
            distance = 1
            shortest_cp = abs(st[i][0] - cp[j][0]) + abs(st[i][1] - cp[j][1])
        elif abs(st[i][0] - cp[j][0]) + abs(st[i][1] - cp[j][1]) < shortest_cp:
            distance = j + 1
            shortest_cp = abs(st[i][0] - cp[j][0]) + abs(st[i][1] - cp[j][1])
    print(distance)
