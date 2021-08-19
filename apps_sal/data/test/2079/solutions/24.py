n = int(input())
line = input().split()
w = []
for i in range(n):
    w.append((int(line[i]), i + 1))
w = sorted(tuple(w))
cur = 0
st = []
res = []
for ch in input():
    if ch == '0':
        st.append(w[cur][1])
        res.append(w[cur][1])
        cur += 1
    else:
        res.append(st[-1])
        st.pop()
print(' '.join((str(item) for item in res)))
