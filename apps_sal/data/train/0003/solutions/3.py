t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    k = int(l[1])
    l = input().split()
    li = [int(i) for i in l]
    if(k == 0):
        print(max(li) - min(li))
        continue
    z = 0
    li.sort()
    li.reverse()
    for i in range(k + 1):
        z += li[i]
    print(z)
