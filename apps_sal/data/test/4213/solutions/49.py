n = int(input())
al = sorted(list(map(int, input().split())))
print(abs(al[0]-al[-1]))
