s = input()
open = '<', '(', '[', '{'
close = '>', ')', ']', '}'
resp = {close[i]: open[i] for i in (0, 1, 2, 3)}
cnt = 0
st = []
flag = True
for c in s:
    if c in open:
        st.append(c)
    elif st and st[-1] == resp[c]:
        st.pop()
    elif st:
        st.pop()
        cnt += 1
    else:
        flag = False
        break
if st: flag = False
print(cnt if flag else 'Impossible')
    


