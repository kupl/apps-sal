N = int(input())
lst = input().split()
D = int(lst[0])

A = []
for i in range(N):
    A.append(int(input()))

count = int(lst[1])

for Ai in A:
    s = 1
    while s <= D:
        count += 1
        s += Ai

print(count)
