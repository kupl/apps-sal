s = input()
m = [2 * [0] for _ in range(2)]
odd, even = 0, 0
for i in range(len(s)):
    m[1 if s[i] == 'a' else 0][i % 2] += 1
    odd += m[1 if s[i] == 'a' else 0][i % 2]
    even += m[1 if s[i] == 'a' else 0][not (i % 2)]

print(even, odd)
