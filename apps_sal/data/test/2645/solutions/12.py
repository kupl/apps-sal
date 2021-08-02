s = list(input())

answer = 0
for i in range(len(s)):
    if i % 2 == 0 and s[i] == "p":
        answer -= 1
    elif i % 2 == 1 and s[i] == "g":
        answer += 1

print(answer)
