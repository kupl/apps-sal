N = int(input())
lst = input().split()

for i in range(N):
   lst[i] = int(lst[i])

print(abs(max(lst) - min(lst)))
