n, k = list(map(int, input().split()))
s = input()

cq = [0] * 26
do = [0] * 26

a = ord('A')

for i in s:
    cq[ord(i) - a] += 1

cntr = 0

for i in s:
    ind = ord(i) - a
    if do[ind] == 0:
        cntr += 1
    do[ind] += 1
    if cntr > k:
        print('YES')
        return
    if do[ind] == cq[ind]:
        cntr -= 1
    

print('NO')

