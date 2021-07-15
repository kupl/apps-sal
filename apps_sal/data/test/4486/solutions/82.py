s = input()
s.split()
odd = []

for i in range(len(s)):
    if i % 2 == 0:
        odd.append(s[i])
answer = ''.join(odd)

print(answer)
