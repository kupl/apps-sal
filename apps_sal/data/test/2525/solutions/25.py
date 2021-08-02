S = input()
top = ''
Q = int(input())
t = 0
for i in range(Q):
    strA = input().split()
    if strA[0] == '1':
        t = t + 1
    else:
        if strA[1] == '1':
            if t % 2 == 0:
                top = top + strA[2]
            else:
                S = S + strA[2]
        else:
            if t % 2 == 0:
                S = S + strA[2]
            else:
                top = top + strA[2]

if t % 2 == 0:
    S = top[::-1] + S
else:
    S = S[::-1] + top
print(S)
