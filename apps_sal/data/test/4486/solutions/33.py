s = input()
odd_num = list()
for i in range(len(s)):
    if i % 2 == 0:
        odd_num.append(s[i])
answer = ''.join(odd_num)
print(answer)
