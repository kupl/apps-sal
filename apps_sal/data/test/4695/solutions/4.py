(X, Y) = map(int, input().split())
A = (1, 3, 5, 7, 8, 10, 12)
B = (4, 6, 9, 11)
C = 2
ans = 'No'
if X in A and Y in A:
    ans = 'Yes'
elif X in B and Y in B:
    ans = 'Yes'
elif X == Y == 2:
    ans = 'Yes'
print(ans)
