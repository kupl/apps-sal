n = int(input())
p = [int(x) for x in input().split()]
ans = []
for i in range(n):
    mask = [0] * n
    st = [i]
    while len(st) > 0:
        a = st.pop()
        if mask[a] == 1:
            ans.append(str(a + 1))
            break
        mask[a] = 1
        st.append(p[a] - 1)
print(' '.join(ans))
