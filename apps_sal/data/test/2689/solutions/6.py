s = input()
st = ""
st2 = ""
for i in range(len(s)):
    if s[i].isdigit():
        st2 = st2 + st
        st = ""
        n = int(s[i])
        continue
    elif s[i] == '+':
        continue
    elif s[i] == '-':
        st = st * n
    else:
        st = st + s[i]

if st != "":
    st2 = st2 + st
if st2[::-1] == st2:
    print("Return")
else:
    print("Continue")
