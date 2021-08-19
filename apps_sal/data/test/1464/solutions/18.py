a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def fed(n):
    for j in a:
        for k in a:
            x = True
            for i in range(n):
                if (j + k in l[i]) == False:
                    x = True
                else:
                    x = False
                    break
            if x == True:
                return j + k


n = int(input())
l = [0] * n
for i in range(n):
    l[i] = input()
s = set([])
for i in range(n):
    s = s | set(l[i])
if s != set(a):
    for j in range(len(a)):
        if (a[j] in s) == False:
            print(a[j])
            break
else:
    print(fed(n))
