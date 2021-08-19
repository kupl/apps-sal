import sys


#sys.stdin = open("input.txt")
#sys.stdout = open("output.txt", "w")

n, m = (int(i) for i in input().split())
ans = 0
for i in range(n):
    lst = [int(j) for j in input().split()]
    for j in range(m):
        if lst[2 * j] == 1 or lst[2 * j + 1] == 1:
            ans += 1
print(ans)
