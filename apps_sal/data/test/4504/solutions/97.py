s=input()
s = list(s)
del s[-1]
del s[-1]
while True:
    if s[:len(s)//2] == s[len(s)//2:]:
        print(len(s))
        return
    else:
        del s[-1]
        del s[-1]
