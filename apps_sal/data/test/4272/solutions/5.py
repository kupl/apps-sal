# 2020/09/18
# AtCoder Beginner Contest 150 - B

# Input
n = int(input())
s = input()
cnt = 0
abc = 'ABC'

# Calc
for i in range(n-2):
    for j in range(3):
        if s[i+j] != abc[j]:
            break
        if j == 2:
            cnt = cnt + 1

# Output
print(cnt)

