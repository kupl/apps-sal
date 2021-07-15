n = int(input())
lst = []
for i in range(n):
    s, p = input().split()
    lst.append([s, -(int(p)), i+1])
lst.sort()
for i in range(n):
    print(lst[i][2])
