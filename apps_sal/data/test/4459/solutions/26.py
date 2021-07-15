import collections
n = int(input())
a = list(map(int,input().split()))

a_cnt = collections.Counter(a)
#print(a_cnt)
cnt = 0
for item in a_cnt.items():
    if item[0]<item[1]:
        cnt += item[1]-item[0]
    elif item[0]>item[1]:
        cnt += item[1]
print(cnt)
