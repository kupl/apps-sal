# 51 C - Many Medians
N = int(input())
X = list(map(int, input().split()))
Xsrt = sorted(X, reverse=False)
XL = set(Xsrt[:N // 2])
XR = set(Xsrt[N // 2:])

ans = []
for x in X:
    if x in XR:
        ans.append(Xsrt[N // 2 - 1])
    elif x in XL:
        ans.append(Xsrt[N // 2])
for a in ans:
    print(a)
