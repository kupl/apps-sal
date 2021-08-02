n = int(input())
A = list(map(int, input().split()))
c = 0
p = 0
for i in range(n):
    if A[i] in [4, 5]:
        c += 1
    else:
        c = 0
    if c == 3:
        p += 1
        c = 0
print(p)
