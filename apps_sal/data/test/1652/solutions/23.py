S = list(input())

A = ['dream', 'dreamer', 'erase', 'eraser']

ans = 'YES'
l = len(S)
while l >= 5:
    if S[l - 5:l] == list(A[0]):
        l -= 5
    elif S[l - 5:l] == list(A[2]):
        l -= 5
    elif l == 5:
        break
    elif S[l - 6:l] == list(A[3]):
        l -= 6
    elif l == 6:
        break
    elif S[l - 7:l] == list(A[1]):
        l -= 7
    else:
        ans = 'NO'
        break
if l != 0:
    ans = 'NO'
print(ans)
