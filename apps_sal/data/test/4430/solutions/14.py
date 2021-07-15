import sys
input = sys.stdin.readline

def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    if min(a) > k:
        return 0
    a = a[::-1]
    current = 0
    answer = 0
    for i in range(n):
        if current + a[i] <= k:
            current += a[i]
            answer += 1
        else:
            current = 0
            m -= 1
            if m == 0:
                break
            else:
                if current + a[i] < k:
                    current += a[i]
                    answer += 1
                elif current + a[i] == k:
                    answer += 1
                    m -= 1
                    if m == 0:
                        break
                else:
                    continue
    return answer
def __starting_point():
    print(main())
__starting_point()
