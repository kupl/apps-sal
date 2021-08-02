N, K = map(int, input().split())
HP = list(map(int, input().split()))

HP.sort()

if K > 0:
    HP = HP[:-K]

print(sum(HP))
