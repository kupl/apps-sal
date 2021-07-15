from collections import *

n, m = map(int, input().split())

a = [int(i) for i in input().split()]

st = set(a)
if len(st) < n:
    print(0);return

mp = defaultdict(int)
for i in a:
    mp[i] += 1

for i in a:
    mp[i] -= 1
    if (mp[i & m] > 0):
        print(1);return
    mp[i] += 1

st.clear()

for i in a:
    t = m
    if (i & t) in st:
        print(2);return
    st.add(i & t)

print(-1)

