S = input()
Q = int(input())
reverse = False
left = ''
right = ''

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        reverse = not reverse
    else:
        F = q[1]
        C = q[2]
        if not reverse:
            if F == '1':
                left = C + left
            else:
                right += C
        else:
            if F == '1':
                right += C
            else:
                left = C + left

S = left + S + right
if not reverse:
    print(S)
    return
else:
    print((S[::-1]))
    return
