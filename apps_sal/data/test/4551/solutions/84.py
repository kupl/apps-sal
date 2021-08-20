(A, B, C, D) = map(int, input().split())
AB = A + B
CD = C + D
if AB > CD:
    print('Left')
elif AB < CD:
    print('Right')
else:
    print('Balanced')
