test_case = int(input())
 
 
def solve():
    a, b = list(map(int, input().split()))
    s = input().split('X')
    lens = [len(dot) for dot in s]
    cnt = 0
    tmp = 0
    for le in lens:
        if le < b:
            continue
        if le < a:
            return "NO"
        if le >= 2 * b:
            if tmp > 0:
                return "NO"
            tmp = le
        else:
            cnt += 1
 
    if tmp is not 0:
        win = False
        for i in range(tmp+1):
            part2 = tmp - i - a
            if i > part2 or i >= 2 * b:
                break
            if 2*b <= part2 or b <= i < a or b <= part2 < a:
                continue
            ncnt = cnt
            if i >= a:
                ncnt += 1
            if part2 >= a:
                ncnt += 1
            if ncnt % 2 is 0:
                win = True
    else:
        win = cnt % 2 == 1
    return "YES" if win else "NO"
 
 
for _ in range(test_case):
    print(solve())

