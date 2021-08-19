n = int(input())
s1 = input().split()
s2 = input().split()
st1 = 0
st2 = 0
for i in range(n):
    if s1[i] == '1':
        st1 = i
    if s2[i] == '1':
        st2 = i
i = (st1 + 1) % n
j = (st2 + 1) % n
f = True
steps = 0
while steps < n:
    if s1[i] == '0':
        i = (i + 1) % n
    if s2[j] == '0':
        j = (j + 1) % n
    if s1[i] != s2[j]:
        f = False
        break
    i = (i + 1) % n
    j = (j + 1) % n
    steps += 1
if f:
    print('YES')
else:
    print('NO')
