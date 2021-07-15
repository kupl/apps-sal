N = int(input())
list1 = list(map(int,input().split()))

list1.sort(reverse=True)

alice = 0
bob = 0
for i in range(len(list1)):
    if i % 2 == 0:
        alice += list1[i]
    else:
        bob += list1[i]

print((alice - bob))

