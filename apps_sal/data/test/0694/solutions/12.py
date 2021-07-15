s = input()
a, b = list(map(int, input().split()))

left = [-1 for i in range(len(s))]
right = [-1 for i in range(len(s))]
x = 0
for i in range(len(s)):
    x = (x * 10 + int(s[i])) % a
    left[i] = x % a
    
x = 0
m = 1
for i in reversed(list(range(0, len(s)))):
    x = (int(s[i]) * m + x) % b
    right[i] = x % b
    m = (m * 10) % b

pos = -1
for i in range(len(s) - 1):
    if left[i] == 0 and right[i + 1] == 0 and s[i + 1] != '0':
        pos = i 
        break
if pos == -1:
    print('NO')
else:
    print('YES')
    print(s[:pos + 1])
    print(s[pos + 1:])

