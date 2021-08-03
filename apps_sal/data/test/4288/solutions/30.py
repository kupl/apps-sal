a, b, c = map(int, input().split())
if(a == b and b == c):
    print('No')
elif(a == b or a == c):
    print('Yes')
elif(b == c):
    print('Yes')
else:
    print('No')
