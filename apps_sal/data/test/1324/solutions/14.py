import sys
#sys.stdin = open('input.txt', 'r')

a = list(map(int, input().split()))
S = input()
k = 0
for s in S:
    k += a[int(s) - 1]
print(k)
