N = int(input())
vA = list(map(int, input().split()))
vAm = sorted([vA[i]-i-1 for i in range(N)])
b = vAm[N//2]
vans = [abs(Am-b) for Am in vAm]
print(sum(vans))
