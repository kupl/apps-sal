n = int(input())
s = input()

inp = False
st, A, B = 0, 0, 0

for c in s:
    if c == '_':
        if st:
            if inp:
                B += 1
            else:
                A = max(A, st)
            st = 0
    elif c == '(':
        assert(not inp)
        if st:
            A = max(A, st)
            st = 0
        inp = True
    elif c == ')':
        assert(inp)
        if st:
            B += 1
            st = 0
        inp = False
    else:
        st += 1

assert(not inp)
if st:
    A = max(A, st)
    st = 0

print(A, B)


