n = input()
l = [int(i) for i in input().split()]

l.sort()

if l[-1] >= l[-2] + l[-3]:
    print("NO")
else:
    print("YES")
    print(l[-1], end=" ")
    print(l[-3], end=" ")
    for k in range(len(l) - 3):
        print(l[k], end=" ")
    print(l[-2])
