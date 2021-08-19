A = []
for i in range(5):
    A.append(int(input()))
k = int(input())
ans = False
for i in range(5):
    for j in range(i + 1, 5):
        if abs(A[i] - A[j]) > k:
            ans = True
            break
if ans == False:
    print('Yay!')
else:
    print(':(')
