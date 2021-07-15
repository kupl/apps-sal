n = int(input())
mywords = []
for i in range(n):
    mywords.append(input())

judge = 0
for i in range(n - 1):
    if not(mywords[i][len(mywords[i]) - 1] == mywords[i + 1][0]):
        judge = 1

for i in range(n):
    if mywords.count(mywords[i]) > 1:
        judge = 1

if judge == 1:
    print("No")
else:
    print("Yes")

