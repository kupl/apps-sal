def get(s):
    ans = 0
    for i in s:
        ans += (ord(i) - ord('0'))
    return ans


def solve1():
    x = input()
    n = len(x)
    best_ans = x
    best_val = get(x)
    ans = str('' if int(x[0]) - 1 == 0 else int(x[0]) - 1) + '9' * (n - 1)
    if get(ans) > best_val or (get(ans) >= best_val and int(ans) > int(best_ans)):
        best_ans = ans
        best_val = get(ans)
    for i in range(1, n):
        #print(ans)
        ans = x[:i] + str(int(x[i]) - 1) + '9' * (n - i - 1)
        if get(ans) > best_val or (get(ans) >= best_val and int(ans) > int(best_ans)):
            best_ans = ans
            best_val = get(ans)
    return best_ans
    
best = [0] * 10000
def solve2():
    nonlocal best
    was = 0
    for i in range(1, 10000):
        if get(str(i)) >= was:
            best[i] = i
            was = get(str(i))
        else:
            best[i] = best[i - 1]
    
def stress():
    solve2()
    for i in range(1, 10000):
        if int(solve1(str(i))) != best[i]:
            print(i, best[i], solve1(str(i)))

#stress()
print(solve1())
