import sys

n = int(sys.stdin.readline())
liste = list(map(int, sys.stdin.readline().split()))
seen = [0]*200
maxi = 0
for loop in range(n):
    seen[liste[loop]] += 1
    maxi = max(maxi, seen[liste[loop]])
print(maxi)
