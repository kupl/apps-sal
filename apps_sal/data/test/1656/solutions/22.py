s = input()
n = len(s)
count_o = []
count_w = 0
count = 0
for i in range(1, n):
    if s[i] == 'v' and s[i-1] == 'v':
        count_w += 1
    elif s[i] == 'o':
        count_o.append(count_w)
for c in count_o:
    count += c * (count_w-c)
print(count)

