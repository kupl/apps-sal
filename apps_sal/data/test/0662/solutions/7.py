n = int(input())
correct = True
A = set([1, 2])
spect = 3
for _ in range(n):
    tmp = int(input())
    if tmp not in A:
        correct = False
        break
    (A, spect) = (set([spect, tmp]), list(A.difference(set([tmp])))[0])
if correct:
    print('YES')
else:
    print('NO')
