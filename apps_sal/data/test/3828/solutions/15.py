n = int(input())
lst = [0 for i in range(n)]
kereta = input().split()
for i in range(n):
    lst[int(kereta[i]) - 1] = i
ancol = 1
terbanyak = 0
for i in range(n - 1):
    if lst[i] > lst[i + 1]:
        if terbanyak < ancol: terbanyak = ancol
        ancol = 0
    ancol += 1
if terbanyak < ancol: terbanyak = ancol
print(n - terbanyak)
