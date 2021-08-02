n = int(input())
a = list(input())
k = 0
st = []
for i in range(n):
    if a[i] == ')' and len(st) > 0 and st[-1][0] == '(':
        k += 2
        st.pop()
    else:
        st.append([a[i], i + 1])
if n % 2 == 1 or len(st) == 0:
    print(0)
elif len(st) == 2 and st[0][0] == st[1][0]:
    if st[0][0] == '(':
        print((n - st[1][1]) // 2 + 1)
    else:
        print(st[0][1] // 2 + 1)
else:
    print(0)
