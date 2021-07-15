n = int(input())
cand = [int(i) for i in input().split()]
opp = cand[1:]
opp.sort()
lemak = cand[0]
result = 0
while lemak <= opp[-1]:
    lemak +=1 
    opp[-1] -= 1
    result += 1
    opp.sort()
print(result)
