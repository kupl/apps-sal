n = int(input())
x = 0
y = 0
s = list(map(int, input().split()))
s.sort()
if(s[n-1]<s[n-2]+s[n-3]):
    print("YES")
    k = []
    l = []
    for i in range(n):
        if(i%2==0):
            k.append(s[n-i-1])
        else:
            l.append(s[n-i-1])
    l.reverse()
    print(" ".join(map(str, l)), " ".join(map(str, k)))
else:
    print("NO")

