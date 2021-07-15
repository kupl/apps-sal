import collections
n = int(input())
num_list = list(map(int, input().split()))
all = 0

c = collections.Counter(num_list)

for i in c:
    all += c[i]*(c[i]-1)//2

for k in range(n):
    print(all - c[num_list[k]] + 1)
