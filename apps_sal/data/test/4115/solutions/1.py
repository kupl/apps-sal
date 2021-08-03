S = input()
num = len(S) // 2
if num % 2 == 0:
    for i in range(num):
        if S[i] == S[-i - 1]:
            num -= 1
else:
    for i in range(num):
        if S[i] == S[-i - 1]:
            num -= 1
print(num)
