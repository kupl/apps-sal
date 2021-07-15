n = int(input())
t = input()
s = 0
for i in range(1, n):
    s += t[i] == t[i - 1]
print(s)
