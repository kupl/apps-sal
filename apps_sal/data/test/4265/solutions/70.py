s = input()
t = input()
S = [x for x in s]
T = [y for y in t]
count = 0
for i in range(len(s)):
    if S[i] != T[i]:
        count += 1
print(count)
