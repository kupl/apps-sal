n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
b = a[:int(len(a) / 2)]
c = a[int(len(a) / 2):]
if(c[0] > b[len(b) - 1]):
    print("YES")
else:
    print("NO")
