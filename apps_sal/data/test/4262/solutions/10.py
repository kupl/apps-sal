from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

count = 0
for i in permutations(sorted(P)):
    if(list(i) == P):
        a = count
    if(list(i) == Q):
        b = count
    count += 1
print((abs(a-b)))

