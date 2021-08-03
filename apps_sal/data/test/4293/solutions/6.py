P, Q, R = map(int, input().split())

if P + Q <= Q + R and P + Q <= P + R:
    print(P + Q)
elif Q + R <= P + Q and Q + R <= P + R:
    print(Q + R)
else:
    print(P + R)
