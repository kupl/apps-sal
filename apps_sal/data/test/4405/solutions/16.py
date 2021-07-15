import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    data_stat = {}
    for i in range(n):
        t = data_stat.get(a[i], 0) + 1
        data_stat[a[i]] = t
    current = sorted(list(data_stat.items()), key = lambda x: x[1])
    answer = 0
    for i in range(1, current[-1][1] + 1):
        pos = len(current) - 1
        cur = i
        res = cur
        while cur % 2 == 0 and pos > 0:
            cur //= 2
            pos -= 1
            if current[pos][1] < cur:
                break
            res += cur
        answer = max(answer, res)
    print(answer)
    return
    
def __starting_point():
    main()

__starting_point()
