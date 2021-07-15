import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = sorted(map(int, input().split()))

last = 0
i = 0
while k:
    if i >= len(a):
        break
    if a[i] - last != 0:
        print(a[i] - last)
        last = a[i]
        k -= 1
    i += 1

for i in range(max(0, k)):
    print(0)
