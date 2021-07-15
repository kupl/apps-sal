S = input()
Q = int(input())
query = [list(input().split()) for _ in range(Q)]
forward = 1
f = ''
b = ''
for i in range(Q):
    if query[i][0] == '1':
        forward *= -1
    else:
        if query[i][1] == '1':
            if forward == 1:
                f += query[i][2]
            else:
                b += query[i][2] 
        else:
            if forward == 1:
                b += query[i][2] 
            else:
                f += query[i][2]
S = ''.join(list(reversed(f))) + S + b

if forward == -1:
    ans = ''.join(list(reversed(S)))
else:
    ans = S
print(ans)

