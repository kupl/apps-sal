N = int(input())
A = list(map(int, input().split()))
maxA = max(A)
minA = min(A)
flag = (abs(maxA) >= abs(minA))
cnt = 0
man = []
if flag:
    idx = A.index(maxA)
    for i in range(len(A)):
        if i != idx:
            man.append([idx + 1, i + 1])
    for i in range(1, len(A)):
        man.append([i, i + 1])

else:
    idx = A.index(minA)
    for i in range(len(A)):
        if i != idx:
            man.append([idx + 1, i + 1])
    for i in range(len(A), 1, -1):
        man.append([i, i - 1])
print((len(man)))
for ma in man:
    print((*ma))
