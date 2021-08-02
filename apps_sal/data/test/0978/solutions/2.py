k = int(input())
a = [0] * 10
for i in range(4):
    s = input()
    for j in range(4):
        if s[j] != '.':
            a[int(s[j])] += 1
ans = 'YES'
for i in range(10):
    if 2 * k < a[i]:
        ans = 'NO'
print(ans)
