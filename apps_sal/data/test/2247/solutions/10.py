# codeforces_1056A_live
def gi(): return list(map(int, input().split()))


for k in range(gi()[0]):
    s, a, b, c = gi()
    print(s // c + ((s // c) // a) * b)
