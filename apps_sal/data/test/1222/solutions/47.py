from collections import deque

def main():
    k = int(input())
    l = list(range(1, 10))
    Q = deque(l)
    for _ in range(k):
        q = Q.popleft()
        # 基準-1
        if q % 10 != 0:
            Q.append(10*q+q%10-1)
        # 基準
        Q.append(10*q+q%10)
        # 基準 + 1
        if q % 10 != 9:
            Q.append(10*q+q%10+1)
    print(q)

def __starting_point():
    main()

__starting_point()
