n = int(input())
s = input()
d = ("a","e","y","u","i","o")
prev = "p"
ans = []
count = 1
for i in range(n):
    if s[i] == prev and s[i] in d:
        count+=1
        if (s[i] == "o" or s[i] == "e") and count == 2:
            if i == len(s)-1:
                ans.append(s[i])
            elif s[i+1] != s[i]:
                ans.append(s[i])
        continue
    ans.append(s[i])
    count = 1
    prev = s[i]
print("".join(ans))
