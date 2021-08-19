# your code goes here
n = int(input())
str = input()

S = 0
prev = str[0]
LEN = len(str)
i = 1
if LEN > 1:
    while i < n:
        if str[i] == prev:
            S += 1
        else:
            prev = str[i]
        i += 1
print(S)
