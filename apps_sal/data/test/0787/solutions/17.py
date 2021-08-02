def output():
    print("YES")

    for st in ans:
        print(st)


k = int(input())
q = input()
n = len(q)

ans = []
used = set()
lim = 1
last = -1
for i in range(n):
    if q[i] not in used:
        if last != -1:
            lim += 1
            ans.append(q[last: i])
        used.add(q[i])
        last = i
    if lim == k:
        ans.append(q[i:])
        output()
        break

if lim < k:
    print("NO")
