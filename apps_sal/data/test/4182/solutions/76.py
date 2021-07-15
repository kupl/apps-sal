N,M,X,Y = (int(T) for T in input().split())
ACityMax = sorted(int(T) for T in input().split())[-1]
BCityMin = sorted(int(T) for T in input().split())[0]
if ACityMax<BCityMin and ACityMax<Y and X<BCityMin:
    print('No War')
else:
    print('War')
