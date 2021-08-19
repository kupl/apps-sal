n, a, b = list(map(int, input().split()))
ls = list(range(1, n + 1))
k = 0
rounds = 0
m = n
while m > 1:
    m >>= 1
    rounds += 1
# print(rounds)
while len(ls) > 1:
    # print(ls)
    k += 1
    newls = []
    for i in range(0, len(ls), 2):
        if (ls[i] == a or ls[i] == b) and (ls[i + 1] == a or ls[i + 1] == b):
            if k == rounds:
                print("Final!")
            else:
                print(k)
            newls = []
            break
        elif ls[i] == a or ls[i + 1] == a:
            newls.append(a)
        elif ls[i] == b or ls[i + 1] == b:
            newls.append(b)
        else:
            newls.append(ls[i])
    ls = newls
