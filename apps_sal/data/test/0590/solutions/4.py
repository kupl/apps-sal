n = int(input())
air = [int(x) for x in input().split()]
a = [0] * (n + 1)
a[0] = 1
for x in range(n):
    a[air[x]] += 1
st = [0]
for x in range(n, -1, -1):
    if a[x] == 0:
        st.append(x)
cnt = 0
level = dict()
for x in range(n):
    if a[air[x]] > 1:
        if air[x] > st[-1]:
            a[air[x]] -= 1
            air[x] = st[-1]
            st.pop()
            cnt += 1
        elif level.get(air[x], 0) == 0:
            level[air[x]] = 1
        else:
            a[air[x]] -= 1
            air[x] = st[-1]
            st.pop()
            cnt += 1
print(cnt)
for x in air:
    print(x, end=' ')
