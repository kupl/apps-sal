import sys
n = int(input())
s = list(map(int, input().split()))
st = set()
for i in s:
    st.add(i)
p = set()
pw = []
for i in range(31):
    p.add(2**i)
    pw.append(2**i)
for i in range(n):
    for j in range(len(pw)):
        if s[i] + pw[j] in st:
            if s[i] - pw[j] in st:
                print(3)
                print(s[i] - pw[j], s[i], s[i] + pw[j])
                return
            if s[i] + pw[j] + pw[j] in st:
                print(3)
                print(s[i], s[i] + pw[j], s[i] + pw[j] + pw[j])
                return
        if s[i] - pw[j] in st:
            if s[i] + pw[j] in st:
                print(3)
                print(s[i] - pw[j], s[i], s[i] + pw[j])
                return
            if s[i] - pw[j] - pw[j] in st:
                print(3)
                print(s[i], s[i] - pw[j], s[i] - pw[j] - pw[j])
                return
for i in range(n):
    for j in range(len(pw)):
        if s[i] + pw[j] in st:
            print(2)
            print(s[i], s[i] + pw[j])
            return
        if s[i] - pw[j] in st:
            print(2)
            print(s[i], s[i] - pw[j])
            return
print(1)
print(s[0])
