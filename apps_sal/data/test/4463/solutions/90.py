s = list(input())
t = list(input())

s.sort()
t.sort(reverse=True)

for i in range(min(len(s), len(t))):
    if(s[i] < t[i]):
        print("Yes")
        return
    if(s[i] > t[i]):
        print("No")
        return

if(len(s) < len(t)):
    print("Yes")
else:
    print("No")
