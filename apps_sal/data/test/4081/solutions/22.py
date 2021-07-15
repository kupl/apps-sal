from collections import deque

def solve(A):
    res = []
    last = 0
    while A:
        if max(A[0],A[-1]) <= last:
            return res

        if A[0] == A[-1]:
            v = A[0]-1
            for i,a in enumerate(A):
                if v < a:
                    v = a
                else:
                    break
            else:
                i += 1
            L = i
            v = A[-1]-1
            for i,a in enumerate(reversed(A)):
                if v < a:
                    v = a
                else:
                    break
            else:
                i += 1
            R = i
            _,op = max((L, ['L']*L), (R, ['R']*R))
            res.extend(op)
            return res
        
        v, op = min((v, op) for v,op in ((A[0], 'L'), (A[-1], 'R')) if v > last)
        last = v
        res.append(op)
        if op == 'L':
            A.popleft()
        else:
            A.pop()


def main():
    input()
    A = deque(map(int,input().split()))

    res = solve(A)
    print(len(res))
    print(*res, sep='')


main()
