def check(dest,start):
    ll = dest[1] - start[1] + dest[2]-start[2]
    if ll < 0:
        ll = -ll
    time = dest[0] - start[0]
    tmp = ll - time
    if tmp <= 0 and tmp%2 == 0 :
        return True
    else:
        return False

n = int(input())
start = [0,0,0]
for i in range(n):
    dest = list(map(int, input().split()))
    if check(dest,start):
        start = dest
    else:
        print("No")
        return

print("Yes")
