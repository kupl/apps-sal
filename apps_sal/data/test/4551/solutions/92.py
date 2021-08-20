(a, b, c, d) = list(map(int, input().split()))
if sum((a, b)) > sum((c, d)):
    print('Left')
elif sum((a, b)) < sum((c, d)):
    print('Right')
else:
    print('Balanced')
