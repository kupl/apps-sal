import heapq
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

x = A.index(-1)
for i in range(x + 1):
    A[i] = 0
B = list(reversed(A))
H = []

ANS = 0
LIST = [0] + [n - (1 << i) + 1 for i in range(n.bit_length() - 1, 0, -1)]
for i in range(1, n.bit_length()):
    for j in range(LIST[i - 1], LIST[i]):
        heapq.heappush(H, B[j])

    # print(H)

    x = heapq.heappop(H)
    ANS += x

print(ANS)
