variant = int(input())
biceps = chest = back = 0
A = list(map(int, input().split()))
for i in range(variant):
    i += 1
    if i % 3 == 1:
        chest += A[i - 1]
    elif i % 3 == 2:
        biceps += A[i - 1]
    else:
        back += A[i - 1]

if chest > biceps:
    if chest > back:
        print("chest")
    else:
        print("back")

else:
    if biceps > back:
        print("biceps")
    else:
        print("back")
