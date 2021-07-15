n, k, q = map(int, input().split())
data = list(map(int, input().split()))
data1 = set()
for i in range(q):
    typ, fr = map(int, input().split())
    fr -= 1
    if typ == 2:
        if data[fr] in data1:
            print("YES")
        else:
            print("NO")
    else:
        if len(list(data1)) < k:
            data1.add(data[fr])
        elif data[fr] >= min(list(data1)):
            data1.add(data[fr])
            data1.remove(min(list(data1)))
