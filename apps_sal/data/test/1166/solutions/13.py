
n = int(input())
a = [int(x) for x in input().split()]

a_reverse = a.copy()
status = []
for i in range(n):
    a_reverse[a[i] - 1] = i
    status.append(None)


pos = a_reverse[n - 1]
status[pos] = False
fails = set()
fails.add(pos)
for i in range(n - 1, 0, -1):
    i_ = i - 1
    pos = a_reverse[i_]
    for k in range((pos + 1) % i - 1, n, i):
        if k == pos:
            continue
        if k in fails:
            status[pos] = True
            break
    if not status[pos]:
        status[pos] = False
        fails.add(pos)


result = ""
for i in status:
    if i == True:
        result = result + "A"
    else:
        result = result + "B"

print(result)
