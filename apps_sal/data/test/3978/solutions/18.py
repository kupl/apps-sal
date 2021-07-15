def calc(X):
    if len(X) == 0:
        return 0
    return calc([x for x in X if x % min(X)]) + 1
    
N = int(input())
print(calc([int(a) for a in input().split()]))



