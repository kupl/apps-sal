import sys
N = int(input())
reward = set()
for i in range(N):
    S = input()
    reward.add(S)
print(len(reward))
