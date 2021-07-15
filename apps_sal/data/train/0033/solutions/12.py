import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        N = int(input())

        x = []
        for i in range(1, N + 1):
            x.append(i)

        print(2)

        while len(x) >= 2:
            a = x.pop()
            b = x.pop()
            c = -(-(a + b) // 2)
            print(a, b)
            x.append(c)

        
    

def __starting_point():
    main()



__starting_point()
