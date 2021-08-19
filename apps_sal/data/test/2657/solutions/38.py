n = int(input())
L = list(map(int, input().split()))
L.sort()
maxL = L[-1]
li = [abs(x - maxL / 2) for x in L]
a = li.index(min(li))
print(maxL, L[a])
