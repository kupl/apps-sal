N = str(input())
S = map(str, input().split())

color = list(S)
factor = set(color)

if len(factor) == 3:
    print("Three")
if len(factor) == 4:
    print("Four")
