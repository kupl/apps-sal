from operator import itemgetter
#int(input())
#map(int,input().split())
#[list(map(int,input().split())) for i in range(q)]
#print("YES" * ans + "NO" * (1-ans))
n = int(input())
ai = list(map(int,input().split()))
ai.sort()
print(min(ai[-2] - ai[0],ai[-1] - ai[1]))

