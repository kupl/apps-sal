n = int(input())
li = list(map(int,input().split()))
li.sort(reverse=True)
alice = []
bob = []
for i in range(n):
    if i % 2 == 0:
        alice.append(li[i])
    else:
        bob.append(li[i])
print(sum(alice)-sum(bob))
