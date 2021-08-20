n = int(input())
s = 0
for _ in range(n):
    s += 1 if input()[1] == '+' else -1
print(s)
