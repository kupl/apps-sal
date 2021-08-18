import sys


n = int(input())
stud = []
for i in range(1, 2 * n):
    lst = [int(x) for x in input().split()]
    for j in range(len(lst)):
        stud += [(lst[j], j, i)]

stud.sort(reverse=True)
ans = [-1 for x in range(2 * n)]

for item in stud:
    first = item[1]
    second = item[2]
    if ans[first] == ans[second] == -1:
        ans[first] = second
        ans[second] = first

for x in ans:
    print(x + 1, end=' ')
print()
