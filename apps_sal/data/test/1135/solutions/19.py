n = int(input())
s = input()
s1 = ''
for i in range(len(s) - 1, -1, -1):
    s1 = s1[:len(s1) // 2] + s[i] + s1[len(s1) // 2:]
print(s1)
