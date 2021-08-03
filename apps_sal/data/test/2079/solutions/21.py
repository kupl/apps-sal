n = int(input())
a = [int(i) for i in input().split()]
s = input()

mp = {}
for i in range(n):
    mp[a[i]] = i + 1
a.sort()

intr = 0
extr = 0
first = mp[a[0]]
st = []
ans = []
for i in range(len(s)):
    if s[i] == '0':
        ans += [mp[a[intr]]]
        st.append(mp[a[intr]])
        intr += 1
    else:
        ans += [st.pop()]
print(*ans)
