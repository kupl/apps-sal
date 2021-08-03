n, k = list(map(int, input().split()))
st = list(input())
g = st.index("G")
t = st.index("T")

if abs(g - t) % k != 0:
    print("NO")
else:
    start = min(g, t)
    end = max(g, t)
    while start != end:
        start += k
        if st[start] == '#':
            print("NO")
            return
    print("YES")
