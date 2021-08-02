# B Polygon
N = int(input())
L = list(map(int, input().split()))
mx = L.pop(L.index(max(L)))
if mx < sum(L):
    print("Yes")
else:
    print("No")
pass
