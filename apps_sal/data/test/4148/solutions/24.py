N = int(input())
S = list(input())
alp = [chr(i) for i in range(65, 65 + 26)] * 2
for j in S:
    num = alp.index(j)
    print(alp[num + N], end="")
