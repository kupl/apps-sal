n, k = list(map(int, input().split()))
s = input()

happy = 0
for i in range(n - 1):
    if s[i] == s[i + 1]:
        happy += 1
print((min(happy + k * 2, n - 1)))
