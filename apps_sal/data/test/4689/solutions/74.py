(k, n) = list(map(int, input().split()))
a = list(map(int, input().split()))
new_a = sorted(a)
num = len(new_a) - 1
s_a = []
b = k - new_a[num] + new_a[0]
s_a.append(b)
cun = 0
for i in new_a[1:]:
    s = i - new_a[cun]
    s_a.append(s)
    cun += 1
max_num = max(s_a)
print(sum(s_a) - max_num)
