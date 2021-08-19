from operator import itemgetter
# int(input())
# map(int,input().split())
#[list(map(int,input().split())) for i in range(q)]
#print("YES" * ans + "NO" * (1-ans))
n = int(input())
if n == 1:
    print(1)
else:
    pi = list(map(int, input().split()))
    ai = [1] * (n + 1)
    ai[0] = 10**9
    for i in pi:
        ai[i] = 0
    for i in range(n - 2, -1, -1):
        ai[pi[i]] += ai[i + 2]
    ai.sort()
    for i in range(n):
        print(ai[i], end=" ")
