MAX_NUM = 10**9
n = int(input())
king_x, king_y = map(int, input().split())
nomakers = {'Rook': {'right-down': [], 'right-up': [], 'left-down': [], 'left-up': []}, 'Bishop': {'left': [], 'right': [], 'up': [], 'down': []}}
yes = {'Queen': {'right-down': [], 'right-up': [], 'left-down': [], 'left-up': [], 'left': [], 'right': [], 'up': [], 'down': []}, 'Bishop': {'right-down': [], 'right-up': [], 'left-down': [], 'left-up': []}, 'Rook': {'left': [], 'right': [], 'up': [], 'down': []}}
for i in range(n):
    figure, figure_x, figure_y = input().split()
    figure_x, figure_y = int(figure_x), int(figure_y)
    if figure == 'Q':
        if figure_x == king_x:
            if figure_y < king_y:
                half = 'down'
            else:
                half = 'up'
            yes['Queen'][half].append(abs(king_y - figure_y))
            for i in range(len(nomakers['Bishop'][half])):
                if nomakers['Bishop'][half][i] < yes['Queen'][half][-1]:
                    del yes['Queen'][half][-1]
                    break
        elif figure_y == king_y:
            if figure_x < king_x:
                half = 'left'
            else:
                half = 'right'
            yes['Queen'][half].append(abs(king_x - figure_x))
            for i in range(len(nomakers['Bishop'][half])):
                if nomakers['Bishop'][half][i] < yes['Queen'][half][-1]:
                    del yes['Queen'][half][-1]
                    break
        elif abs(figure_x - king_x) == abs(figure_y - king_y):
            if figure_x > king_x:
                if figure_y > king_y:
                    quarter = 'right-up'
                else:
                    quarter = 'right-down'
            else:
                if figure_y > king_y:
                    quarter = 'left-up'
                else:
                    quarter = 'left-down'
            yes['Queen'][quarter].append(abs(king_x - figure_x))
            for i in range(len(nomakers['Rook'][quarter])):
                if nomakers['Rook'][quarter][i] < yes['Queen'][quarter][-1]:
                    del yes['Queen'][quarter][-1]
                    break
    elif figure == 'R':
        if figure_x == king_x:
            if figure_y < king_y:
                half = 'down'
            else:
                half = 'up'
            yes['Rook'][half].append(abs(king_y - figure_y))
            for i in range(len(nomakers['Bishop'][half])):
                if nomakers['Bishop'][half][i] < yes['Rook'][half][-1]:
                    del yes['Rook'][half][-1]
                    break
        elif figure_y == king_y:
            if figure_x > king_x:
                half = 'right'
            else:
                half = 'left'
            yes['Rook'][half].append(abs(king_x - figure_x))
            for i in range(len(nomakers['Bishop'][half])):
                if nomakers['Bishop'][half][i] < yes['Rook'][half][-1]:
                    del yes['Rook'][half][-1]
                    break
        elif abs(figure_x - king_x) == abs(figure_y - king_y):
            if figure_x > king_x:
                if figure_y > king_y:
                    quarter = 'right-up'
                else:
                    quarter = 'right-down'
            else:
                if figure_y > king_y:
                    quarter = 'left-up'
                else:
                    quarter = 'left-down'
            nomakers['Rook'][quarter].append(abs(figure_x - king_x))
            i = 0
            n = len(yes['Queen'][quarter])
            while i < n:
                element = yes['Queen'][quarter][i]
                if nomakers['Rook'][quarter][-1] < element:
                    del yes['Queen'][quarter][i]
                    n = n - 1
                else:
                    i = i + 1
            i = 0
            n = len(yes['Bishop'][quarter])
            while i < n:
                element = yes['Bishop'][quarter][i]
                if nomakers['Rook'][quarter][-1] < element:
                    del yes['Bishop'][quarter][i]
                    n = n - 1
                else:
                    i = i + 1
    else:
        if abs(figure_x - king_x) == abs(figure_y - king_y):
            if figure_x > king_x:
                if figure_y > king_y:
                    quarter = 'right-up'
                else:
                    quarter = 'right-down'
            else:
                if figure_y > king_y:
                    quarter = 'left-up'
                else:
                    quarter = 'left-down'
            yes['Bishop'][quarter].append(abs(figure_x - king_x))
            for i in range(len(nomakers['Rook'][quarter])):
                if nomakers['Rook'][quarter][i] < yes['Bishop'][quarter][-1]:
                    del yes['Bishop'][quarter][-1]
                    break
        elif figure_x == king_x or figure_y == king_y:
            if figure_y < king_y:
                a = figure_y - king_y
                half = 'down'
            elif figure_y > king_y:
                half = 'up'
                a = figure_y - king_y
            elif figure_x > king_x:
                a = figure_x - king_x
                half = 'right'
            else:
                a = figure_x - king_x
                half = 'left'
            nomakers['Bishop'][half].append(abs(a))
            i = 0
            n = len(yes['Rook'][half])
            while i < n:
                element = yes['Rook'][half][i]
                if nomakers['Bishop'][half][-1] < element:
                    del yes['Rook'][half][i]
                    n = n - 1
                else:
                    i = i + 1
            i = 0
            n = len(yes['Queen'][half])
            while i < n:
                element = yes['Queen'][half][i]
                if nomakers['Bishop'][half][-1] < element:
                    del yes['Queen'][half][i]
                    n = n - 1
                else:
                    i = i + 1
if len(yes['Queen']['left']) > 0 or len(yes['Queen']['right']) > 0 or len(yes['Queen']['down']) > 0 or len(yes['Queen']['up']) > 0 or len(yes['Queen']['left-up']) > 0 or len(yes['Queen']['left-down']) > 0 or len(yes['Queen']['right-up']) > 0 or len(yes['Queen']['right-down']) > 0 or len(yes['Bishop']['right-down']) > 0 or len(yes['Bishop']['right-up']) > 0 or len(yes['Bishop']['left-up']) > 0 or len(yes['Bishop']['left-down']) > 0 or len(yes['Rook']['left']) > 0 or len(yes['Rook']['right']) > 0 or len(yes['Rook']['up']) > 0 or len(yes['Rook']['down']) > 0:
    print("YES")
else:
    print("NO")
