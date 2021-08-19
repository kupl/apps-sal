N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
alice = 0
bob = 0
tf = True
for i in a:
    if tf:
        alice += i
    else:
        bob += i
    tf = not tf
print(alice - bob)
