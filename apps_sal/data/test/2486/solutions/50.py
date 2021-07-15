import sys
input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse = True)

subtotal = 0
need = 0
for i in range(N):
    if subtotal + a[i] < K:
        subtotal += a[i]
    else:
        need = i+1
print(N - need)
