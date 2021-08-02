from operator import itemgetter
n, k = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * 5001
for i in range(n):
    x = a[i]
    c[x] += 1

flag = 0
ar = [([0] * 3) for i in range(n)]
for i in range(n):
    ar[i][0] = a[i]
    ar[i][1] = i

ar = sorted(ar, key=itemgetter(0))
# print(ar)
for i in range(5001):
    if(c[i] > k):
        flag = 1
        break

if(flag == 0):
    co = 1
    for i in range(n):
        if(co > k):
            co = 1
        ar[i][2] = co
        co += 1
    print("YES")
    ar = sorted(ar, key=itemgetter(1))
    for i in range(n):
        print(ar[i][2], end=" ")

    print()

else:
    print("NO")
