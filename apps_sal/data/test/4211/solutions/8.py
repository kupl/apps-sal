n = int(input())
#a, b = map(int, input().split())
bl = list(map(int, input().split()))
#al=[list(input()) for i in range(n)]

al = [0]*n
al[-1] = bl[-1]
for i in range(n-2, -1, -1):
    if bl[i] < al[i+1]:
        al[i+1] = bl[i]
    al[i] = bl[i]
print((sum(al)))

