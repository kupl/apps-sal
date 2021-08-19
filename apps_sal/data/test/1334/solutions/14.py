(n, k) = input().split()
(n, k) = (int(n), int(k))
s = list(input())
st = s[:k]
s.sort()
a = [s[0]]
b = True
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        a.append(s[i])
while len(st) < k:
    st.append(a[0])
    b = False
if b:
    for i in reversed(range(k)):
        if st[i] != a[len(a) - 1]:
            for j in range(len(a) - 1):
                if st[i] == a[j]:
                    st[i] = a[j + 1]
                    break
            for j in range(i + 1, k):
                st[j] = a[0]
            break
stri = ''
for r in st:
    stri = stri + r
print(stri)
