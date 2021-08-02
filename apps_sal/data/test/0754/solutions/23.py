n = int(input())
t = input()
m = 0
for i in range(1, n):
    m += t[i] == t[i - 1]
print(m)
