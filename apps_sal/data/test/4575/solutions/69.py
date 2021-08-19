N = int(input())
(D, X) = map(int, input().split())
A = [int(input()) for _ in range(N)]
count = 0
for a_i in A:
    count += len(list(range(1, D + 1, a_i)))
print(count + X)
