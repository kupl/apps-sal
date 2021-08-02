a = input()
b = input()
num_n = [0]
num_one = [0]
for elem in a:
    if elem == '1':
        num_one.append(num_one[-1] + 1)
        num_n.append(num_n[-1])
    else:
        num_one.append(num_one[-1])
        num_n.append(num_n[-1] + 1)
res = 0
la = len(a)
lb = len(b)
for i in range(lb):
    left = max(0, i - lb + la)
    right = min(la - 1, i)
    if b[i] == '1':
        res += num_n[right + 1] - num_n[left]
    else:
        res += num_one[right + 1] - num_one[left]
print(res)
