import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
n = int(input())
res = [int(t) for t in input().split()]
res.sort()
min_erase = n
i, j = 0, 0
while i != n - 1:
    if res[j] <= 2 * res[i]:
        ans = True
        if n - (j - i + 1) < min_erase:
            min_erase = n - (j - i + 1)
    else:
        ans = False
    if ans and j != n - 1:
        j += 1
    else:
        i += 1
print(min_erase)
