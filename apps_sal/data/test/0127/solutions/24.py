import sys

# sys.stdin = open('in', 'r')

n, f = list(map(int, input().split()))

arr = []

ans = 0

for line in sys.stdin:
    k, l = list(map(int, line.split()))
    inc = min(k * 2, l) - k
    ans += min(k, l)
    arr.append(inc)

arr.sort(reverse=True)

for i in range(f):
    if(arr[i] > 0):
        ans += arr[i]

print(ans)
