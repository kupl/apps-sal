n1, b1 = list(map(int, input().split()))
ans1 = 0
a1 = list(map(int, input().split()))
n2, b2 = list(map(int, input().split()))
ans2 = 0
a2 = list(map(int, input().split()))
for i in range(n1):
    ans1 += a1[i] * (b1 ** (n1 - i - 1))
for i in range(n2):
    ans2 += a2[i] * (b2 ** (n2 - i - 1))
if (ans1 == ans2):
    print('=')
else:
    if ans1 > ans2:
        print('>')
    else:
        print('<')
