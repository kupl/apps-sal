s = input()
canw = 0
canb = 0
for i in range(len(s)):
    if i % 2 == 1:
        if s[i] == '1':
            canw += 1
        else:
            canb += 1
    elif i % 2 == 0:
        if s[i] == '1':
            canb += 1
        else:
            canw += 1

print(min(canb, canw))
