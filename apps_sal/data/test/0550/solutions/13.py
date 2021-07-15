ss = input()
st = ""
for j in range(len(ss)):
    c = ss[j]
    if 'A' <= c <= 'Z':
        c = chr(ord(c) + ord('a') - ord('A'))
    if c == 'o':
        c = '0'
    if c == 'l' or c == 'i':
        c = '1'
    st += c
s = st
n = int(input())
for i in range(n):
    ss = input()
    st = ""
    for j in range(len(ss)):
        c = ss[j]
        if 'A' <= c <= 'Z':
            c = chr(ord(c) + ord('a') - ord('A'))
        if c == 'o':
            c = '0'
        if c == 'l' or c == 'i':
            c = '1'
        st += c
    if s == st:
        print("No")
        return
print("Yes")

