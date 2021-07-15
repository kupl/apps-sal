t = int(input())
for i in range(t):
    n = int(input())
    st2 = 4
    while n % (st2 - 1) != 0:
        st2 *= 2
    print(n // (st2 - 1))
