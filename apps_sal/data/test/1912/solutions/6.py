import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        R, G, B, W = [int(x) for x in input().split()]
        if R % 2 + G % 2 + B % 2 + W % 2 <= 1:
            print("Yes")
        else:
            if R >= 1 and G >= 1 and B >= 1:
                R -= 1
                G -= 1
                B -= 1
                W += 3
                if R % 2 + G % 2 + B % 2 + W % 2 <= 1:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")

        
    

def __starting_point():
    main()



__starting_point()
