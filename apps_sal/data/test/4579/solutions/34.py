n = int(input())
s = [''] * n
for i in range(n):
    s[i] = input()
print(len(set(s)))
