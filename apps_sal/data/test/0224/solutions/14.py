import math,sys,re,itertools,pprint,collections
ri,rai=lambda:int(input()),lambda:list(map(int, input().split()))

s = input()
t = list([len(x) for x in re.split(r"[AEIOUY]+", s)])

print(max(t) + 1)

