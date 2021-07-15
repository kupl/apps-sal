S = input()
for i in range(26):
    c = chr(i + 97)
    prev = -3
    for j in range(len(S)):
        if S[j] == c:
            if j - prev <= 2:
                print(prev + 1, j + 1)
                break
            prev = j
    else:
        continue
    break
else:
    print(-1, -1)
