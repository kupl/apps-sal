n = int(input())
a = []
for _ in range(n):
    a.append(int(input()))
b = a.copy()
b.sort()
a_ = max(a)
for i in range(n):
    if a[i] == a_:
        print(b[-2])
    else:
        print(a_)
