3

n = int(input())
lst = [input() for _ in range(n)]
alf = [chr(ord('a') + _) for _ in range(26)]
ans = None
for a in alf:
    if not [1 for w in lst if w.find(a) != -1]:
        ans = a
        break
if ans is not None:
    print(ans)
else:
    for a in alf:
        for b in alf:
            t = a + b
            if not [1 for w in lst if w.find(t) != -1]:
                ans = t
                break
        if ans is not None:
            print(ans)
            break

