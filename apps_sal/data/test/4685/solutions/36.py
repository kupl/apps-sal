lst = input().split()
K = int(input())
for i in range(3):
   lst[i] = int(lst[i])

print(sum(lst) + (max(lst) *  ((2 ** K) - 1)))
