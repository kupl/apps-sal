S = input()

D =[]
for i in range(3):
    if S[i] == S[i+1]:
        D.append(1)
        break


if 1 in D:
    print("Bad")

else:
    print("Good")

