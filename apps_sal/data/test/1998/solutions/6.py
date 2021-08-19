'''input
5 4 1 0
00000
'''
from sys import stdin
import collections
import math


def get_working(string):
    aux = []
    first = None
    if string[0] == 1:
        pass
    else:
        first = -1
    for i in range(len(string)):
        if string[i] == '1':
            if first == None:
                first = i
            elif first != None:
                aux.append([first, i, (i - first - 1)])
                first = i
    if first != None:
        aux.append([first, len(string), (len(string) - first) - 1])

    return aux


# main starts
n, a, b, k = list(map(int, stdin.readline().split()))
string = list(stdin.readline().strip())

ans = 0
working = get_working(string)
# print(working)
current = a
flag = 0
for i in working:
    if flag == 1:
        break
    start, end, gap = i

    j = end - 1
    if gap // b > 0:
        while j > start:
            if current == 0:
                flag = 1
                break
            if (j - start) // b > 0:
                for k in range(j, j - b, -1):
                    string[k] = '2'
                j -= b
                current -= 1
            else:
                break
ans = []
count = 0
for i in range(len(string)):
    if string[i] == '0':
        if i > 0 and string[i - 1] == '0':
            count += 1
        else:
            count = 1

        if count == b:
            string[i] = 'b'
            ans.append(i + 1)
            count = 0


for i in range(len(string)):
    if string[i] == '2':
        ans.append(i + 1)
        break
# print(string)
print(len(ans))
print(*ans)
# print(ans)
# for i in range(n):
# 	if string[i] == 'b':
# 		print(i + 1, end = ' ')
