n, m = map(int, input().split())
ls = [int(i) for i in input().split()]

t = sorted(ls)
t.reverse()
ans = 0
st = []
for i in range(m):
    ans += t[i]
    st.append(t[i])

print(ans)

l = -1
for i in range(n):
    if ls[i] in st:
        if len(st) == 1:
            print(n - 1 - l)
            return

        st.pop(st.index(ls[i]))
        print(i - l, end=' ')
        l = i
