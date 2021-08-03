s = input()
k = int(input())

answer = 1
if len(s) == 1:
    answer = s
else:
    for i in range(k):
        if s[i] != "1":
            answer = s[i]
            break
print(answer)
