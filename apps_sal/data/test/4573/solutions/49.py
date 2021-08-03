N = int(input())
X = list(map(int, input().split()))
org = X.copy()

X.sort()

right = int(N // 2)
left = right - 1

med = (X[left] + X[right]) / 2

for x in org:
    if x >= med:
        print((X[left]))
    else:
        print((X[right]))
