temp = input().strip().split()
n = int(temp[0])
c = int(temp[1])

pVals = input().strip().split()
tVals = input().strip().split()
pVals = [int(stng) for stng in pVals]
tVals = [int(stng) for stng in tVals]

l = 0
mins = 0
for i in range(n):
    mins = mins + tVals[i]
    l = l + max(0, pVals[i] - c*mins)

r = 0
mins = 0
for i in range(n-1, -1,-1):
    mins = mins + tVals[i]
    r = r + max(0, pVals[i] - c*mins)

if l > r:
    print("Limak")
elif r > l:
    print("Radewoosh")
else:
    print("Tie")
