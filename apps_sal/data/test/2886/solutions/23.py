s = input()
x = len(s)
for i in range(x-2):
    n = s[i:i+3]
    m = list(set(n))
    if len(m) == 2:
        print(i+1,i+3)
        return
if x == 2:
    if s[0] == s[1]:
        print(1,2)
        return
print(-1,-1)
