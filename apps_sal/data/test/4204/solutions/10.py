# coding = SJIS

s = str(input())
k = int(input())

ans = 1

for i in range(k):
    if s[i] != "1":
        print(s[i])
        return

print(ans)
