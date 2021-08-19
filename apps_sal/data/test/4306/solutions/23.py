import re
import copy


def accept_input():
    (ast, aen, bst, ben) = list(map(int, input().split()))
    return (ast, aen, bst, ben)


def process(s):
    if s == '#':
        return 1
    else:
        return 0


(ast, aen, bst, ben) = accept_input()
if ast >= bst and ast <= ben:
    print(min(ben, aen) - ast)
elif ast < bst:
    if aen < bst:
        print(0)
    else:
        print(min(aen, ben) - bst)
else:
    print(0)
