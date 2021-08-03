a = input().split()
n = int(a[0])
k = int(a[1])
v = list(map(int, input().split()))
s = 0
co = 1
cur_s = 0
cur = 0
dal = k - 1
for i in range(k):
    cur_s += v[i]
s += cur_s

while (dal + 1 < n):
    co += 1
    cur_s -= v[cur]
    cur += 1
    dal += 1
    cur_s += v[dal]
    s += cur_s
print(s / co)
