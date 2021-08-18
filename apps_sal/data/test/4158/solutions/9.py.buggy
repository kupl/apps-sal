st = set([])
n = int(input())
arr = map(int, input().split())
maxn = int(1e9)
ans = 0
lol1 = lol2 = 0

for i in arr:
    st.add(i)
for i in st:
    p = 1
    while i + p <= maxn:
        if i + p in st:
            if i + p + p in st:
                print(3)
                print(i, end=" ")
                print(i + p, end=" ")
                print(i + p + p)
                return
            else:
                ans = 2
                lol1 = i
                lol2 = i + p
        p *= 2
if ans == 2:
    print(2)
    print(lol1, end=" ")
    print(lol2)
else:
    print(1)
    print(st.pop())
