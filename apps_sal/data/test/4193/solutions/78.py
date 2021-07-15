#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline

def bingo_check(card):
    #横チェック
    for low in card:
        if sum(low)==0:
            print("Yes")
            return
    #縦チェック
    column1=0
    column2=0
    column3=0
    for low in card:
        column1+=low[0]
        column2+=low[1]
        column3+=low[2]
    if column1 == 0 or column2 == 0 or column3==0:
        print("Yes")
        return
    #斜めチェック
    diagonal1=card[0][0]+card[1][1]+card[2][2]
    diagonal2=card[0][2]+card[1][1]+card[2][0]
    if diagonal1 == 0 or diagonal2 == 0:
        print("Yes")
        return
    print("No")

def main():
    bingo=[]
    use_card=[]
    bingo=[list(map(int,input().split())) for _ in range(3)]
    use_card=bingo
    n = int(input())

    for idx in range(n):
        number=int(input())
        for i in range(3):
            for j in range(3):
                if number==use_card[i][j]:
                    use_card[i][j]=0
                else:
                    continue
    bingo_check(use_card)

def __starting_point():
    main()
__starting_point()
