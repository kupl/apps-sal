from operator import itemgetter
n = int(input())
ai = list(map(int, input().split()))
ai.sort()
print(min(ai[-2] - ai[0], ai[-1] - ai[1]))
