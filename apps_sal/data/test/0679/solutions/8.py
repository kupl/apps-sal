s = input()
n = len(s)
ans = ['A', 'B', 'C']
for i in range(1, n - 1):
    t = [s[i - 1], s[i], s[i + 1]]
    t.sort()
    if t == ans:
        print('Yes')
        return
print("No")
