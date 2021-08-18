import sys

n = int(input())
a = list(map(int, input().split()))
prev2 = -1
prev = a[0]
sol = 0
for x in a[1:]:
    if x + prev == 5:
        print("Infinite")
        return
    if x == 1:
        if prev == 2:
            sol += 3
        if prev == 3:
            sol += 4
    if x == 2:
        sol += 3
        if prev2 == 3:
            sol -= 1
    if x == 3:
        sol += 4
    prev2 = prev
    prev = x
print("Finite")
print(sol)
