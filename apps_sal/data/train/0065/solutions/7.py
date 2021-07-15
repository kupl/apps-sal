from math import ceil

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        enemies = list(map(int, input().split()))
        j = 0
        c = 1
        ans = 0
        while j < n:
            if c:
                c = 0
                if enemies[j] == 1:
                    ans += 1
                    j += 1
                if j < n and enemies[j] == 0:
                    j += 1
            else:
                c = 1
                if enemies[j] == 1:
                    j += 1
                if j < n and enemies[j] == 1:
                    j += 1
        print(ans)


main()
