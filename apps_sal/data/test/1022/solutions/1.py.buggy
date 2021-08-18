n = int(input())

l = list(map(int, input().split()))
r = list(map(int, input().split()))

a = [[l[i] + r[i], i] for i in range(n)]
a.sort()
# print(a)
candies = [0 for i in range(n)]

if(a[0][0] != 0):

    print('NO')
    return
else:
    candies[a[0][1]] = n - a[0][0]

for i in range(1, n):
    if(a[i][0] != a[i - 1][0] and a[i][0] != i):
        print('NO')
 #       print(i,a[i])
        return
  #  print(a[i][1],n-a[i][0],i)
    candies[a[i][1]] = n - a[i][0]
# print(candies)
for i in range(n):
    l1 = 0
    r1 = 0
    for j in range(i):
        if(candies[j] > candies[i]):
            l1 += 1
    for j in range(i + 1, n):
        if(candies[j] > candies[i]):
            r1 += 1
 #   print(l1,r1)
    if(l1 != l[i] or r1 != r[i]):
        print('NO')
        return
print('YES')
print(*candies)
