# 53 B
data = list(input())
i = 0
j = 1
while data[i] != 'A':
    i = i + 1
while (data[-j] != 'Z' and len(data) - j > i):
    j = j + 1
print(len(data) - i - j + 1)
