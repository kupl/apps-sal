n, q = list(map(int, input().split()))
s = input()
sl = [0]
for i in range(1, n):
    if s[i-1:i+1] == 'AC':
        sl.append(sl[i-1]+1)
    else:
        sl.append(sl[i-1])

for _ in range(q):
    l, r = list(map(int, input().split()))
    print((sl[r-1]-sl[l-1]))

