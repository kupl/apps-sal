n = int(input())
s = input()
mx = -1
for i in range(1,n):
    x = set(s[0:i])
    y = set(s[i:])
    mx = max(mx,len(x&y))
print(mx)
    

