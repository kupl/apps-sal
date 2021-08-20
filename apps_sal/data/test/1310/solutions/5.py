n = int(input())
st = input()
lis = st.split()
for i in range(n):
    lis[i] = int(lis[i])
lisRes = []
for i in range(n):
    res = lis[i]
    lisRes.append(res)
    for j in range(i + 1, n):
        res ^= lis[j]
        lisRes.append(res)
print(max(lisRes))
