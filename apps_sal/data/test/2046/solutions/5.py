n = int(input())
a_s = map(int, input().split())
ad = {a: i for (i, a) in enumerate(a_s)}
cd = 0
st = []
for i in range(n, 0, -1):
    if ad[i] > cd:
        print(' '.join(st), end='')
        st = []
        print('\n' * (ad[i] - cd), end='')
        cd = ad[i]
    st.append(str(i))
print(' '.join(st))
