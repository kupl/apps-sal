a = 0
b = 0
for i in range(5):
    s = input().split()
    for j in range(5):
        if s[j] == '1':
            a = i + 1
            b = j + 1
print(abs(a-3)+abs(b-3))

