import traceback

def push(stack, delta):
    if stack:
        _, d, mn, mx = stack[-1]
    else:
        d, mn, mx = 0, 0, 0
    stack.append((delta, d + delta, min(d + delta, mn), max(d + delta, mx)))

def main():
    n = int(input())
    ss = input()
    left = [(0, 0,0,0)]
    right = [(0, 0,0,0)] * n
    res = []
    try:
        for s in ss:
            if s == 'R':
                delta = right.pop()[0]
                push(left, -delta)
            elif s == 'L':
                if len(left) > 1:
                    delta = left.pop()[0]
                    push(right, -delta)
            else:
                if left:
                    left.pop()
                if s == '(':
                    delta = 1
                elif s == ')':
                    delta = -1
                else:
                    delta = 0
                push(left, delta)
            _, ld, lmn, lmx = left[-1]
            _, rd, rmn, rmx = right[-1]
            if ld == rd and lmn >= 0 and rmn >= 0:
                res.append(max(ld, lmx, rmx))
            else:
                res.append(-1)
    except Exception as e:
        print(e)
        traceback.print_exc()
        print("size left %d size right %d"%(len(left), len(right)))
    print(' '.join(map(str, res)))




def __starting_point():
    main()
__starting_point()
