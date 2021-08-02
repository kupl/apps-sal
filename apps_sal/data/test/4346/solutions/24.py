tc = int(input())
for i in range(tc):
    x = input().split(" ")
    L = int(x[0])
    v = int(x[1])
    l = int(x[2])
    r = int(x[3])
    print(L // v - r // v + (l - 1) // v)
