n = int(input())
s = input()
i = 0
ans = 0
while i < n:
    if s[i:i+2] == 'UR' or s[i:i+2] == 'RU':
        i+=1
    i+=1
    ans +=1
print(ans)
