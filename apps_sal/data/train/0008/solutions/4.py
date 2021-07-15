from sys import stdin

t = int(stdin.readline())
for i in range(t):
    n, k = tuple(int(x) for x in stdin.readline().split())
    line = 'L' * (k+1) + stdin.readline()[:-1] + 'L' * (k+1)
    score = 0
    flag = False
    for char in line:
        if char == 'W':
            if flag:
                score += 2
            else:
                score += 1
                flag = True
        else:
            flag = False
            
    seq = sorted(len(x) for x in line.split('W'))

    if len(seq) == 1:
        if k == 0:
            print(0)
        else:
            print(2*k-1)
        continue
    for item in seq:
        if item == 0:
            continue
        if k - item >= 0:
            k -= item
            score += 2 * (item-1) + 3
        elif k > 0:
            score += 2 * k
            break
        else:
            break
    print(min(score, 2*n-1))
    

