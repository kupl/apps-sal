n = int(input())
a = [int(e) for e in input().split()]
st = set()
for i in a:
    st.add(i)
b = sorted(list(st))
if len(st) > 3:
    print(-1)
elif len(st) == 3:
    if b[0] + b[2] == b[1] * 2:
        print(b[1] - b[0])
    else:
        print(-1)
elif len(st) == 2:
    if (b[1] - b[0]) % 2 == 0:
        print((b[1] - b[0]) // 2)
    else:
        print(b[1] - b[0])
else:
    print(0)
