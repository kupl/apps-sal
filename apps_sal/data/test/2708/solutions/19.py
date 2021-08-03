(A, B) = list(map(int, input().split(' ')))
for i in range(B):
    if str(A)[-1] != '0':
        A -= 1
    else:
        A //= 10
print(A)
