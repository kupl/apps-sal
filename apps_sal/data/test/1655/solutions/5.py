from sys import stdin, stdout
from random import randrange

n = int(stdin.readline())
counting = [0 for i in range(n + 10)]
values = list(map(int, stdin.readline().split()))

for i in range(n):
    v = values[i]
    counting[max(0, i - v)] += 1
    counting[i] -= 1

cnt = n
for i in range(n):
    counting[i] += counting[i - 1]
    
    if counting[i]:
        cnt -= 1

stdout.write(str(cnt))
