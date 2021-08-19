n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
a_max = max(a)
a_max_cnt = a.count(a_max)
for i in range(n):
    if a[i] != a_max or a_max_cnt > 1:
        print(a_max)
    else:
        print(max(a[:i] + a[i + 1:]))
