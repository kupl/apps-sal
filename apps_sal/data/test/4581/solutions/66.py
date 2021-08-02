S = str(input())

cost = 700
if S[0] == "o":
    cost += 100
if S[1] == "o":
    cost += 100
if S[2] == "o":
    cost += 100

print(cost)
