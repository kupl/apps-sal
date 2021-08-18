
q = int(input())

for i in range(0, q):
    n = int(input())
    ln = [int(j) for j in input().split(" ")]
    st = 0
    f = True
    for j in range(1, len(ln)):
        if abs(ln[j] - ln[j - 1]) != 1 and abs(ln[j] - ln[j - 1]) != n - 1:
            f = False
            break
    if abs(ln[0] - ln[-1]) != 1 and abs(ln[0] - ln[-1]) != n - 1:
        f = False
    if f:
        print("YES")
    else:
        print("NO")
