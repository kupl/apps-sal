n = int(input())
a = list(map(int, input().split()))
b = [[0, 0]]
e = o = 0
for i in range(n):
    if i % 2 == 0:
        o += a[i]
    else:
        e += a[i]
    b.append([e, o])
ans = 0
# print(b)
for i in range(n):
    if i % 2 == 0:
        o1 = b[i][1]
        e1 = b[i][0]
        o = b[-1][0] - e1 + o1
        e = b[-1][1] - a[i] - o1 + e1
    else:
        o1 = b[i][1]
        e1 = b[i][0]
        o = b[-1][0] - e1 + o1 - a[i]
        e = b[-1][1] - o1 + e1
    if o == e:
        ans += 1
    # print(o,e,o1,e1,ans)
print(ans)
