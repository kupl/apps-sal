s = str(input())

n = len(s)

ss = ['A', 'H', 'I', 'M', 'O','o','T','U','V','v','W','w','X','x','Y']
ss2 = [('d','b'),('q','p'),('p','q'),('b','d')]

for i in range(0, n//2):
    if s[i]==s[n-1-i]:
        if not (s[i] in ss):
            print("NIE")
            return
    else:
        if not ((s[i],s[n-1-i]) in ss2):
            print("NIE")
            return

if n%2 != 0:
    if s[n//2] in ss:
        print("TAK")
    else:
        print("NIE")
else:
    print("TAK")




