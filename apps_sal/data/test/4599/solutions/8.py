n = int(input())
a = list(map(int, input().split()))

Alice = []
Bob = []
a.sort()
a.reverse()

for x in range(n):
    if x % 2 == 0:
        Alice.append(a[x])
    else:
        Bob.append(a[x])

print(sum(Alice) - sum(Bob))
