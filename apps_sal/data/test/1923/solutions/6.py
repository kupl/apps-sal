N = int(input())
L = list(map(int,input().split()))
L = sorted(L)

print(sum(L[::2]))
