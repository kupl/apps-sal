n = int(input())

s = input()

ss = ""

i = 0
longest = 0

for i in range(int(n / 2)):
    # print(s[0:i+1])
    # print(s[i+1:i+i+1+1])
    if s[0:i + 1] == s[i + 1:i + i + 1 + 1]:
        longest = i

ans = n - longest

print(ans)
