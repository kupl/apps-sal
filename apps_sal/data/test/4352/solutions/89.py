(A, B) = map(int, input().split())
cA = (A + 12) % 14
cB = (B + 12) % 14
if cA > cB:
    print('Alice')
elif cA == cB:
    print('Draw')
else:
    print('Bob')
