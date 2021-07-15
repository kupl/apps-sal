def readIntArray():
    return list(map(int,input().split()))

t = int(input())
for _ in range(t):
    n, x = readIntArray()
    a = readIntArray()
    st = set()
    for val in a:
        st.add(val)
    ans = 0
    for i in range(1, 300):
        if i not in st:
            if x == 0:
                break
            else:
                x -= 1
                ans += 1
        else:
            ans += 1
    print(ans)
