p = input()  # name
s = input()
answer = 0
j = 0
mini = 0
maxi = 0
lengthP = len(p)
lengthS = len(s)
for i in range(lengthS):
    if s[i] == p[j]:
        j += 1
        if j == lengthP:
            j = 0
            answer += 1
            if answer == 1:
                mini = i
if answer > 1:
    j = lengthP - 1
    for i in range(lengthS - 1, -1, -1):
        if s[i] == p[j]:
            j -= 1
            if j == -1:
                maxi = i
                break
if answer == 1 or answer == 0:
    print(0)
else:
    print(maxi - mini)
