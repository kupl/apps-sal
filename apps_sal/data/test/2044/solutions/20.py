# codeforces_1016A_live
def gi(): return list(map(int, input().split(" ")))


n, m = gi()
line = gi()
acc = 0
for k in range(n):
    acc += line[k]
    print(acc // m, end=" ")
    acc %= m
