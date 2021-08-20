a = input()
b = input()
bo = b.count('1')
lb = len(b)
ao = a[:lb].count('1')
final_ans = 0
if (ao + bo) % 2 == 0:
    final_ans += 1
for i in range(len(a) - lb):
    if a[i] == '1':
        ao -= 1
    if a[i + lb] == '1':
        ao += 1
    if (ao + bo) % 2 == 0:
        final_ans += 1
print(final_ans)
