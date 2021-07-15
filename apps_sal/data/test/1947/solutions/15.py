import sys
input = sys.stdin.readline

def main():
    n, m, l = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    used = set()
    current = 0
    for i in range(n):
        if a[i] > l:
            if i in used:
                continue
            elif (i - 1) not in used and (i + 1) not in used:
                current += 1
            elif (i - 1) in used and (i + 1) in used and (s[1] - 1) not in used:
                current -= 1
            used.add(i)
        d[i] = a[i]
    for i in range(m):
        s = list(map(int, input().split()))
        if s[0] == 0:
            print(current)
        elif s[0] == 1:
            d[s[1] - 1] += s[2]
            if d[s[1] - 1] > l:
                if (s[1] - 1) in used:
                    continue
                elif (s[1] - 2) not in used and (s[1]) not in used:
                    current += 1
                elif (s[1] - 2) in used and (s[1]) in used and (s[1] - 1):
                    current -= 1
                used.add(s[1] - 1)
                
def __starting_point():
    main()
__starting_point()
