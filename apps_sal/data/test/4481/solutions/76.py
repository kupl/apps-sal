import collections
N = int(input())
s = [str(input()) for i in range(N)]
c = collections.Counter(s)
maximum = max(c.values())
max_c_list = sorted(key for key, value in c.items() if value == maximum)
for s in max_c_list:
    print(s)
