n = int(input())
a = list(map(int, input().split()))
(t1, t2, t3, t4) = (0, 0, 0, 0)
for i in range(len(a)):
    if a[i] == 1:
        t1 += 1
        t3 = max(t3 + 1, t2 + 1)
    else:
        t2 = max(t2 + 1, t1 + 1)
        t4 = max(t4 + 1, t3 + 1)
print(max(t1, t2, t3, t4))
