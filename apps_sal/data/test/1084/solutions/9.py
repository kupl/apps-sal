n, m = [int(i) for i in input().split()]
a, b, flag = [-1] * m, list(), True
for i in range(n):
    s = input()
    q = set()
    for j in range(len(s)):
        if s[j] == "
           q.add(j)
    for j in range(len(s)):
        if s[j] == "
           if a[j] == -1:
                a[j] = i
            else:
                if b[a[j]] != q:
                    flag = False
    b.append(q)
if flag:
    print("Yes")
else:
    print("No")
