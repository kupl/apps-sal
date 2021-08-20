N = int(input())
L = sorted(map(int, input().split()))
ret = 0
for i in range(N):
    ret += L[2 * i]
print(ret)
