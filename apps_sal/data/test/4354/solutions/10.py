n, m = map(int, input().split())
st = []
co = []
for i in range(n):
    a, b = map(int, input().split())
    st.append([a, b])
for i in range(m):
    c, d = map(int, input().split())
    co.append([c, d])
for a, b in st:
    tmp = 10**9
    output = 0
    for i in range(m):
        if tmp > (new := abs(a - co[i][0]) + abs(b - co[i][1])):
            output = i + 1
            tmp = new
    print(output)
