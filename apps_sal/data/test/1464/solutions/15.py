n = int(input())
ch = ''
while n:
    sh = input()
    ch += ' ' + sh
    n -= 1
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
t = False
for x in l:
    if x not in ch:
        t = True
        print(x)
        break
if not t:
    for i in range(len(l)):
        if not t:
            for j in range(len(l)):
                s = l[i] + l[j]
                if s not in ch:
                    print(s)
                    t = True
                    break
