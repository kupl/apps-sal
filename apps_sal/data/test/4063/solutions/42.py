n = int(input())
L = sorted(list(map(int,input().split())))
c = n // 2
print(L[c]-L[c-1])
