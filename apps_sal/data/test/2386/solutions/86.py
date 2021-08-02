import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
lst = []
for n in range(1, N + 1):
    lst.append(A[n] - n)
lst.sort()
median = lst[N // 2]
ans = sum([abs(x - median) for x in lst])
print(ans)
