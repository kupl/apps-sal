n, m = list(map(int, input().split()))

alist = list(map(int, input().split()))

blist = list(map(int, input().split()))

prefixsum = [0]

for i in range(n):
    prefixsum.append(alist[i] + prefixsum[-1])
# print(prefixsum)
ptr = 1
for i in range(m):
    while blist[i] > prefixsum[ptr]:
        ptr += 1

    room = blist[i] - prefixsum[ptr - 1]
    print(ptr, room)
