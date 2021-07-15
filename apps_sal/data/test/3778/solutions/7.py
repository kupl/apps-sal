n = int(input())

a = [0] + list(map(int, input().split()))

b = []
poss = True

ones = []
twos = []
threes = []

row_num = n


for c in range(n, 0, -1):
    if a[c] == 0:
        continue

    elif a[c] == 1:
        ones.append((row_num, c))
        b.append((row_num, c))
        row_num -= 1

    elif a[c] == 2:
        if len(ones) > 0:
            q = ones.pop()
            b.append((q[0], c))

            twos.append((q[0], c))
            
        else:
            poss = False

    elif a[c] == 3:
        if len(threes) > 0:
            q = threes.pop()

            b.append((row_num, c))
            b.append((row_num, q[1]))
            threes.append((row_num, c))
            
            row_num -= 1
            
        elif len(twos) > 0:
            q = twos.pop()

            b.append((row_num, c))
            b.append((row_num, q[1]))
            threes.append((row_num, c))
            
            row_num -= 1


        elif len(ones) > 0:
            q = ones.pop()

            b.append((row_num, c))
            b.append((row_num, q[1]))
            threes.append((row_num, c))
            
            row_num -= 1

        else:
            poss = False

if poss:
    print(len(b))
    for item in b:
        print(item[0], item[1])
else:
    print(-1)
    

