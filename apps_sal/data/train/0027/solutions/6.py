t = int(input())
for g in range(t):
    n = int(input())
    st = set()
    a = [int(i) for i in input().split()]
    for i in range(n):
        q = a[i]
        while q % 2 == 0:
            st.add(q)
            q //= 2
    print(len(st))
