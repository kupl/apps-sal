n = int(input())
L = list(map(int, input().split()))
L.sort()
s = sum(L[::2])
print(s)
