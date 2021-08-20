def readIntArray():
    return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n = int(input())
    a = readIntArray()
    mp = {}
    for val in a:
        if val not in mp:
            mp[val] = 0
        mp[val] += 1
    l1 = max(a)
    l2 = n - l1
    if l2 <= 0:
        print(0)
        continue
    good = True
    for i in range(1, l2 + 1):
        if i not in mp or mp[i] != 2:
            good = False
            break
    for i in range(l2 + 1, l1 + 1):
        if i not in mp or mp[i] != 1:
            good = False
            break
    if not good:
        print(0)
        continue
    mp = {}
    ans = set()
    cur = 0
    st = set()
    used = set()
    for i in range(n):
        if a[i] in used:
            break
        st.add(a[i])
        used.add(a[i])
        while cur + 1 in st:
            st.remove(cur + 1)
            cur += 1
        if cur == l1 or (cur == l2 and len(st) == 0):
            ans.add((cur, n - cur))
    print(len(ans))
    for val in ans:
        print(val[0], val[1])
