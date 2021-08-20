(N, X) = [int(i) for i in input().split()]
LS = [int(i) for i in input().split()]
s = 0
cnt = 1
for l in LS:
    s += l
    if s <= X:
        cnt += 1
    else:
        break
print(cnt)
