l, r, k = map(int, input().split())
st = 1
fl = False
while (st <= r):
    if (st >= l and st <= r):
        print(st, end=" ")
        fl = True
        st *= k
    else:
        st *= k
if not fl:
    print(-1)
