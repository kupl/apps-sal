from sys import stdin, stdout # only need for big input


def solve():
    n = int(input()) 
    pos = []
    for _ in range(n):
        t, x, y = list(map(int, input().split()))
        pos.append((t,x,y))

    prev = (0, 0, 0)

    for p in pos:
        dt = p[0] - prev[0]
        move = abs(p[1] - prev[1]) + abs(p[2] - prev[2])
        if move > dt:
            print("No")
            return
        else:
            if (dt - move) % 2 == 1:
                print("No")
                return
            prev = p

    print("Yes")

    
    

def main():
    solve()


def __starting_point():
    main()
__starting_point()
