a = int(input())
for i in range(a):
    b = int(input())
    c = input()
    l = c.find('1')
    r = c.rfind('1')
    if l == -1:
        print(b)
    else:
        k1 = r + 1
        k2 = b - l
        print(max(k1, k2) * 2)
