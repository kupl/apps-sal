import sys
# sys.stdin.readline()
#n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
ans = []
for kek in range(k):
    (a, b) = map(int, sys.stdin.readline().split())
    if a == b:
        ans.append(0)
        continue
    if b > a:
        (a, b) = (b, a)
    kek = 0
    while a % 8 == 0 and a // 8 >= b:
        a //= 8
        kek += 1
    while a % 4 == 0 and a // 4 >= b:
        a //= 4
        kek += 1
    while a % 2 == 0 and a // 2 >= b:
        a //= 2
        kek += 1
    if a != b:
        ans.append(-1)
    else:
        ans.append(kek)
print(*ans, sep='\n')
