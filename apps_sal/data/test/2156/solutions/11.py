n = int(input())
si = list(map(int,input().split()))
q = int(input())
si2 = [0] * (n+1)
for i in range(n):
    si2[i+1] = si2[i] + si[i]
for i in range(q):
    l, r = list(map(int,input().split()))
    print((si2[r]-si2[l-1])//10)

