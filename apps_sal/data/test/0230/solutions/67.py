# 141_E
n = int(input())
s = input()

x = 0
for i in range(n):
    s_ = s[:i + 1]
    if s_[i - x:] in s_[: i - x]:
        x += 1

print(x)
