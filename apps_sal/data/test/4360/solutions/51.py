N = int(input())
A = list(map(int, input().split()))
bunbo = 0
for a in A:
    bunbo += 1 / a
print(1 / bunbo)
