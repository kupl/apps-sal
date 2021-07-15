import sys
sys.setrecursionlimit(4100000)
import math
import fractions



'''
1行のint
N, K = map(int, input().split())

1行のstring
S, T = input().split()

1行の整数配列
P = list(map(int,input().split()))

複数行2数値
x = []
y = []
for i in range(5):
    x1,y1=[int(i) for i in input().split()]
    x.append(x1)
    y.append(y1)

'''


S = input()


check = len(S)-1

while(check >= 0):

    if S[check] == "r":
        if S[check-2] == "m":
            remove = S[check-6: check+1]
            if remove == "dreamer":
                check -= 7
            else:
                print("NO")
                return


        elif S[check-2] == "s":
            remove = S[check-5: check+1]
            
            if remove == "eraser":
                check -= 6
            else:
                print("NO")
                return

        else:
            print("NO")
            return

    elif S[check] == "e":
        remove = S[check-4: check+1]
            
        if remove == "erase":
            check -= 5
        else:
            print("NO")
            return

    elif S[check] == "m":
        remove = S[check-4: check+1]
            
        if remove == "dream":
            check -= 5
        else:
            print("NO")
            return

    else:
        print("NO")
        return


print("YES")
