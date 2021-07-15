c = list(map(int,input().split()))
sum = 0
s = input().strip()
for i in range (len(s)):
    sum += c[int(s[i])-1]
print(sum)
                

