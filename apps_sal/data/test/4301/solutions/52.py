n = int(input())
a = []
for i in range(n):
    A = int(input())
    a.append(A)
a_1 = list(set(a))[-1]
if a.count(a_1) >= 2:
    for i in range(n):
        print(a_1)
else:
    a_2 = list(set(a))[-2]
    for i in range(n):
        if a[i] == a_1:
            print(a_2)
        else:
            print(a_1)
