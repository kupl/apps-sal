n = int(input())
l1 = [input() for i in range(n)]
l2 = []
for i in range(n):
    if l1[i] in l2:
        print("YES")
    else:
        print("NO")
        l2.append(l1[i])
