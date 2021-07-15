from sys import stdin, stdout


n, k = list(map(int, stdin.readline().rstrip().split()))

pebbleList = [int(a) for a in stdin.readline().rstrip().split()]

nTrips=[]
for i in range(n):
    nTrips.append(pebbleList[i]//k)
    if pebbleList[i]%k!=0:
        nTrips[i]+=1

total = sum(nTrips)//2 + sum(nTrips)%2
print(total)

