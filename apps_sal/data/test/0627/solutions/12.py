n = int(input())
s = [i for i in input()]
for i in range(n - 1):
    if s[i] > s[i + 1]:
        s.pop(i)
        break
if len(s) == n:
    s.pop()
print(''.join(s))
