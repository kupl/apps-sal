"""
    CodeForces 368B
    Fly, Freebies, Fly!
"""
n = int(input())
l = [int(x) for x in input().split()]
T = int(input())
l.sort()
M = 1
inz = 0
fin = 1
count = 1
while fin < n:
    while fin < n and l[fin] - l[inz] <= T:
        count += 1
        fin += 1
    if count > M:
        M = count
    inz += 1
    count -= 1
    if fin < inz:
        fin = inz
        count = 1
print(M)
