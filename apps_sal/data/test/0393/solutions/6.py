n = int(input())
n += 2
st = input()
st = '0'+  st + '0'
cond = True
for i in range(1, n):
    if st[i] == st[i - 1] and st[i] == '1':
        cond = False
if cond and (st.count('000') == 0):
    print('Yes')
else:
    print('No')

