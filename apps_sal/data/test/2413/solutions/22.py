t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    mnj = s.find('1')
    mxj = s.rfind('1')
    if mnj == -1:
        print(n)
    else:
        print(max(n - mnj, mxj + 1) * 2)
