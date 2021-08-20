n = int(input())
alist = [int(x) for x in input().split()]
psum = 0
l = 0
lim = sum(alist) // 3
ways = 0
if sum(alist) % 3 != 0:
    print(0)
    quit()
for i in range(n - 1):
    psum += alist[i]
    if psum == 2 * lim:
        ways += l
    if psum == lim:
        l += 1
print(ways)
