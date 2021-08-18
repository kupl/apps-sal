n, s, t = [int(x) for x in input().split()]
p = [int(x) for x in input().split()]
s -= 1
t -= 1
if s == t:
    print(0)
    return
cnt = 0
for i in range(n):
    next = p[s]
    if next == -1:
        break
    p[s] = -1
    s = next - 1
    cnt += 1
    if s == t:
        print(cnt)
        return
print(-1)
