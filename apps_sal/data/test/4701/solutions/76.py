n = int(input())
k = int(input())
mn = 1
for i in range(n):
    if mn + k <= mn * 2:
        mn += k
    else:
        mn = mn * 2
print(mn)
