import sys

N = int(sys.stdin.readline())

arr = []
for i in range(N):
    [L, R] = [int(i) for i in sys.stdin.readline().split()]
    arr.append([R, L])

arr.sort()
last = arr[0][0]
count = 1

for c in range(1, N):
    if(arr[c][1] > last):
        count += 1
        last = arr[c][0]

print(count)
