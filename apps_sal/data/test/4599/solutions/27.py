n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
num = len(a)
alice = []
bob = []
coun = 1
for i in a:
    if coun % 2 == 1:
        alice.append(i)
    else:
        bob.append(i)
    coun += 1
ans = abs(sum(alice) - sum(bob))
print(ans)
