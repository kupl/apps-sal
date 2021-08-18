n = int(input())
L = [int(_) for _ in input().split()]
alive = 0
claw = 0
for i in range(len(L) - 1, -1, -1):
    if claw == 0:
        alive += 1
        claw = L[i]
    else:
        claw -= 1
        if L[i] > claw:
            claw = L[i]
print(alive)
