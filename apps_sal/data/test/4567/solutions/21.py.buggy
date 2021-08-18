n = int(input())
l = [int(input())for _ in range(n)]
l.sort()
ans = sum(l)
if ans % 10 != 0:
    print(ans)
    return
for s in l:
    if (ans - s) % 10 != 0:
        print((ans - s))
        return
print((0))
