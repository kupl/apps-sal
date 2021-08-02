N, Q = [int(i) for i in input().split()]
S = input()
lst = [0]
for x in range(1, len(S)):
    if S[x - 1:x + 1] == "AC":
        lst.append(lst[x - 1] + 1)
    else:
        lst.append(lst[x - 1])

for q in range(Q):
    l, r = [int(i) for i in input().split()]
    print(lst[r - 1] - lst[l - 1])
