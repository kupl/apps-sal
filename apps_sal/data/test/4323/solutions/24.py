
def mi():
    return map(int, input().split())


n, m = mi()
diff = [0] * n
s1 = 0
s2 = 0
for i in range(n):
    n1, n2 = mi()
    s1 += n1
    s2 += n2
    diff[i] = n1 - n2
diff.sort()
if s2 > m:
    print(-1)
else:
    diff.sort(reverse=True)
    c = 0
    for i in diff:
        if s1 <= m:
            break
        s1 -= i
        c += 1
    print(c)
