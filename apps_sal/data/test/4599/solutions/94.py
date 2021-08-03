N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
flag = 0
alice = 0
bob = 0
for i in range(N):
    if flag == 0:
        alice += a[i]
        # print("alice:"+str(alice))
        flag = 1
    else:
        bob += a[i]
        # print("bob:"+str(bob))
        flag = 0
print(alice - bob)
