N = int(input())
lst = input().split()
for i in range(N):
    lst[i] = int(lst[i])
print(max(lst) - min(lst))
