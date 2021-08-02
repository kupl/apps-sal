N = int(input())
Hlist = list(map(int, input().split()))
sign = 1
Answer = 'Yes'
for i in range(len(Hlist) - 1):
    H1 = Hlist[i]
    H2 = Hlist[i + 1]
    if H1 > H2:
        if H1 - H2 == 1 and sign == 1:
            Hlist[i] -= 1
            sign = 0
        else:
            Answer = 'No'
            break
    if H1 < H2:
        sign = 1
print(Answer)
