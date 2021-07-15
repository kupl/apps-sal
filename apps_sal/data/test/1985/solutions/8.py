k, n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
st = set()
zn = b[0]
sums = [a[0]]
for j in range(1, len(a)):
    sums.append(sums[-1] + a[j])
for j in sums:
    st.add(b[0] - j)
for i in b: # �� ��� ������
    tmp = set()
    for j in sums: #�����
        tmp.add(i - j)
        
    st = st.intersection(tmp)
    #print(st)
    if len(st) == 0:
        break
print(len(st))
        

