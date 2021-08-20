from collections import defaultdict
n = int(input())
l = [int(x) for x in input().split()]
dic = defaultdict(int)
for x in l:
    dic[x] += 1
first = dic[1]
second = dic[2] + dic[3]
third = dic[4] + dic[6]
N = len(l)
if 7 in l:
    print('-1')
elif not (first == N // 3 and second == N // 3 and (third == N // 3)):
    print('-1')
elif dic[6] < dic[3]:
    print('-1')
else:
    for _ in range(dic[4]):
        print('1 2 4')
    for _ in range(dic[6] - dic[3]):
        print('1 2 6')
    for _ in range(dic[3]):
        print('1 3 6')
