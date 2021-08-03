# coding = SJIS

n = int(input())

for i in range(n):
    if int((n - i) ** 0.5) == (n - i) ** 0.5:
        print((n - i))
        return
