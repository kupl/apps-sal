import sys
import collections
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
nums = [0 for i in range(n)]
day = 0
match = 0
flag = True
queue = collections.deque([])
temp = set()
for i in range(1, n + 1):
    i2 = a[i - 1][0]
    if a[i2 - 1][0] == i:
        if i not in temp:
            queue.append([i, i2])
            temp.add(i)
            temp.add(i2)
if not queue:
    flag = False
while queue:
    temp = []
    while queue:
        test = queue.popleft()
        match += 1
        (num1, num2) = (test[0], test[1])
        nums[num1 - 1] += 1
        nums[num2 - 1] += 1
        temp.append(num1)
        temp.append(num2)
    flag2 = False
    temp2 = set()
    for i in temp:
        if nums[i - 1] <= n - 2:
            new_num = a[i - 1][nums[i - 1]]
            if nums[new_num - 1] <= n - 2 and a[new_num - 1][nums[new_num - 1]] == i:
                if i not in temp2:
                    queue.append([i, new_num])
                    flag2 = True
                    temp2.add(i)
                    temp2.add(new_num)
    if flag2 == False and match < n * (n - 1) // 2:
        flag = False
        break
    day += 1
if flag == True:
    print(day)
else:
    print(-1)
