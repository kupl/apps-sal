Messages, Max, Last = 0, 0, 0
for i in range(int(input())):
    X = list(map(int, input().split()))
    Messages = max(0, Messages - (X[0] - Last))
    Messages += X[1]
    Max = max(Messages, Max)
    Last = X[0]
print(Last + Messages, Max)

# UB_CodeForces
# Advice: Falling down is an accident, staying down is a choice
# Location: Mashhad for few days
# Caption: Finally happened what should be happened
# CodeNumber: 692
