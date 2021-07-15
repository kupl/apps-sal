s = input()
ans = []

for i in range(len(s)-2):
    number = int(s[i] + s[i+1] + s[i+2])
    ans.append(abs(number - 753))

print(min(ans))
