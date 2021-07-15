A, B = map(int, input().split())
S = list(input())
AB = [0]*2
f = 0
for s in S:
    if s == "-" :
        f = 1
        continue
    AB[f] += 1
if AB[0] == A and AB[1] == B:
    print("Yes")
else:
    print("No")
