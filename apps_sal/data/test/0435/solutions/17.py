n, k = list(map(int, input().split()))
s = input()
ansa = 0
a = 0
b = 0
starta = 0
for i in range(0, n):
    if(s[i] == 'a'):
        a += 1
    else:
        b += 1
    if(min(a, b) > k):
        if(s[starta] == 'a'):
            a -= 1
        else:
            b -= 1
        starta += 1
    else:
        ansa += 1
print(ansa);

