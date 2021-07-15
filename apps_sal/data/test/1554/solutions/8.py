ans = []
s = set()
l = 1
n = input()
for i, e in enumerate(map(int, input().split()), 1):
    if e in s:
        s = set()
        ans += [(l, i)]
        l = i + 1
    else:
        s.add(e)
if ans:
    print(len(ans))
    ans[-1] = ans[-1][0], n
    for a, b in ans:
        print(a, b)
else:
    print(-1)
