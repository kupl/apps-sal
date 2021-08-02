a = list(input())
b = list(reversed(a))
ans_f = 0
ans_r = 0
for i in range(len(a) - 1):
    if a[i] == a[i + 1]:
        a[i + 1] = str(abs(int(a[i]) - 1))
        ans_f += 1
for i in range(len(a) - 1):
    if b[i] == b[i + 1]:
        b[i + 1] = str(abs(int(b[i]) - 1))
        ans_r += 1
print(min(ans_f, ans_r))
