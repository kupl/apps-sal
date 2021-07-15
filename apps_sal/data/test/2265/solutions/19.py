a = input()
b = input()
q = 0 # a > b
for i in b:
    if i == '1':
        q += 1
value = [0] * (len(a) + 1)
lenb = len(b)
ans = 0
for i in range(len(a)):
    value[i + 1] = value[i] + bool(a[i] == '1')
    if i + 1 >= lenb and (abs(value[i + 1] - value[i + 1 - lenb]) - q) % 2 == 0:
        ans += 1
print(ans)

