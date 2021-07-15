cal = list(map(int,input().split()))
s = input()
tot = 0
for i in range(len(s)):
    tot += cal[int(s[i])-1]
print(tot)

