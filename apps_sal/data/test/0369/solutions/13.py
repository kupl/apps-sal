import sys
def input(): return sys.stdin.readline().strip()

def main():
    N, M = map(int, input().split())
    S = input()

    def isOK(index):
        return S[index] == "0"
    
    ans = []
    now = N
    while now:
        for step in range(min(now, M), -1, -1):
            if step == 0:
                print(-1)
                return

            if isOK(now-step):
                ans.append(step)
                now -= step
                break
    print(*ans[::-1], sep=" ")



def __starting_point():
    main()
__starting_point()
