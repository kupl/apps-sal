def main():
    card = [[int(j) for j in input().split()] for i in range(3)]
    n = int(input())
    def punch(v):
        for i in range(len(card)):
            for j in range(len(card[i])):
                if card[i][j] == v:
                    card[i][j] = True
        return card

    def check(board):
        for i in range(len(board)):
            l = list(set(board[i]))
            if len(l)==1 and l[0] ==True:
                return True
        for i in range(len(board[0])):
            if board[0][i] == board[1][i]==board[2][i] == True:
                return True
        if board[0][0] == board[1][1]==board[2][2] == True:
            return True
        if board[0][2] == board[1][1]==board[2][0] == True:
            return True

    for _ in range(n):
        num = int(input())
        if check(punch(num)):
            return "Yes"
    return "No"


    print(card)

def __starting_point():
    print(main())
__starting_point()
