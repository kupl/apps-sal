import sys
n = int(input())
l = list(map(int, input().split()))
wyn = 0
for i in range(1, n):
    if l[i] == 1 and l[i - 1] == 2:
        wyn += 3
    if l[i] == 1 and l[i - 1] == 3:
        wyn += 4
    if l[i] == 2 and l[i - 1] == 1:
        wyn += 3
    if l[i] == 2 and l[i - 1] == 3:
        print("Infinite")
        return
    if l[i] == 3 and l[i - 1] == 1:
        wyn += 4
    if l[i] == 3 and l[i - 1] == 2:
        print("Infinite")
        return
for i in range(2, n):
    if l[i - 2] == 3 and l[i - 1] == 1 and l[i] == 2:
        wyn -= 1
print("Finite")
print(wyn)
