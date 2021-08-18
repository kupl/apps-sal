def last(i, find, finish):
    while dict_a[find] != finish:
        keys_a[i] = dict_a[find]
        find = keys_a[i]
        i += 2


n = int(input())
dict_a = {}
dict_b = {}
for i in range(n):
    c = input().split()
    dict_a[int(c[0])] = int(c[1])
    dict_b[int(c[1])] = None

keys_a = sorted(dict_a.keys())
dict_b = sorted(dict_b.keys())

pos = 0
while keys_a[pos] == dict_b[pos]:
    pos += 1
start = keys_a[pos]
end = dict_b[pos]

while (pos + 1 < n) and (dict_b[pos + 1] == start):
    start = keys_a[pos + 1]
    pos += 1
while (pos + 1 < n) and (keys_a[pos + 1] == end):
    end = dict_b[pos + 1]
    pos += 1

keys_a = [start] + [0] * (n - 2) + [end]
dict_b = None

if n % 2 == 0:
    last(2, start, 0)
    last(1, 0, end)
else:
    last(2, start, end)
    last(1, 0, 0)

for i in range(n - 1):
    print(keys_a[i], end=' ')
print(keys_a[n - 1])
