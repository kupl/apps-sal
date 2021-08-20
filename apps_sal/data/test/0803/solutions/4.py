n = int(input())
s = input()
diff = (s.count('x') - s.count('X')) // 2
print(abs(diff))
s = list(s)
for i in range(len(s)):
    if s[i] == 'X' and diff < 0:
        s[i] = 'x'
        diff += 1
    elif s[i] == 'x' and diff > 0:
        s[i] = 'X'
        diff -= 1
print(''.join(s))
