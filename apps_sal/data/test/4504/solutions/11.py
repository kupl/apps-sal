S = input()
for i in range(1, len(S)):
    s = S[0:len(S) - i]
    if len(s) % 2 == 1:
        continue
    if s[0:int(len(s) / 2)] == s[int(len(s) / 2):len(s)]:
        print(len(S) - i)
        break
