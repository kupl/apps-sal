def inpl(): return [int(i) for i in input().split()]
def minich(A, plus):
    ans = 0
    back = 0
    for i in A:
        if plus:
            if back + i < 0:
                back = back + i
            else:
                ans += back + i + 1
                back = -1
        else:
            if back + i > 0:
                back = back + i
            else:
                ans += 1 - back - i
                back = 1
        plus = not plus
    return ans
N = int(input())
A = inpl()
print(min(minich(A, True), minich(A, False)))
