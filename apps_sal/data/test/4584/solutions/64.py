N = int(input())
A = list(map(int, input().split()))
buka = [0] * N
for a in A:
    buka[a - 1] += 1
for x in buka:
    print(x)
