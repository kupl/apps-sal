(A, B, X) = map(int, input().split())


def judge(x):
    if A * x + B * len(str(x)) <= X:
        return True
    else:
        return False


sta = 0
fin = X
while fin - sta > 1:
    m = (fin + sta) // 2
    if judge(m) == True:
        sta = m
    else:
        fin = m
if sta > 10 ** 9:
    print(10 ** 9)
else:
    print(sta)
