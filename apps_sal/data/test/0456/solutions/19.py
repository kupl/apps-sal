n = int(input())
s = input()
for i in range(50,-1,-1):
    cool_s = 'ogo'+i*'go'
    while cool_s in s:
        s = s[:s.find(cool_s)]+'***'+s[s.find(cool_s)+len(cool_s):]
print(s)
