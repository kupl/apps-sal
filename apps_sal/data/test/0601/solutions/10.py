from math import  ceil, sqrt

def main():
    t = int(input())
    for i in range(t):
        p, f = map(int, input().split())
        count_a, count_b = map(int, input().split())
        a, b = map(int, input().split())
        if a > b:
            a, b = b, a
            count_a, count_b = count_b, count_a
        ans = 0
        for i in range(count_a + 1):
            if i * a > p:
                break
            l = min(count_b, (p - i * a) // b)
            r = min(f // a, count_a - i)
            g = min(count_b - l, (f - r * a) // b)
            ans = max(ans, i + l + r + g)
        print(ans)

main()
