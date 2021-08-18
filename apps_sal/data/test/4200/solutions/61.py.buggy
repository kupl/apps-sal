import sys

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())), reverse=True)

all_vote = sum(A)

for i in range(M):
    if A[i] < all_vote / (4 * M):
        print("No")
        return

print("Yes")
