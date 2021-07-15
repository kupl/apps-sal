from math import ceil 
N = int(input())
votes = [1,1]
rate = 1
for i in range(N):
    t,a = map(int,input().split())
    rate = max((votes[0] - 1) // t, (votes[1] - 1) // a) + 1
    # if t * rate >= votes[0] and a * rate >= votes[1]:
    votes = [t * rate, a * rate]

print(sum(votes))
