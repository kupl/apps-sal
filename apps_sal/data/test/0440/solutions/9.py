n = int(input())
s = input()
gl = "aeiouy"
t=True
for i in range(n):
    if s[i] not in gl:
        print(s[i],end="")
        t = True
    elif t:
        print(s[i],end="")
        t = False
