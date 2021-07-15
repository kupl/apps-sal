a = input().split()
st = set([])
cnt = [[0 for i in range(9)] for i in range(3)]
for e in a:
    cnt['mps'.index(e[1])][int(e[0]) - 1] = 1
    st.add(e)
answ = len(st) - 1
for i in range(3):
    for j in range(7):
        answ = min(answ, 3 - sum(cnt[i][j:j + 3]))
print(answ)
