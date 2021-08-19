N = int(input())
(*X,) = map(int, input().split())
s = sorted(X)
t1 = s[N // 2 - 1]
t2 = s[N // 2]
for x in X:
    if x <= t1:
        print(t2)
    else:
        print(t1)
