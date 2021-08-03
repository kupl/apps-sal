def read(): return list(map(int, input().split()))


a, b = read()
Q = [a]
prev = dict()
st = 0
while st < len(Q):
    cur = Q[st]
    st += 1
    if cur * 2 <= b:
        Q.append(cur * 2)
        prev[cur * 2] = cur
    if cur * 10 + 1 <= b:
        Q.append(cur * 10 + 1)
        prev[cur * 10 + 1] = cur
if prev.get(b) is None:
    print('NO')
    return
print('YES')
ans = []
cur = b
while cur != a:
    ans.append(cur)
    cur = prev[cur]
ans.append(a)
print(len(ans))
print(*ans[::-1])
