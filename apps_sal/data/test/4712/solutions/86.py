def resolve():
    '''
    code here
    '''
    H, W = [int(item) for item in input().split()]
    grid = [input() for _ in range(H)]
    
    print(('#'*(W+2)))
    for line in grid:
        print(('#' + line + '#'))
    print(('#'*(W+2)))

def __starting_point():
    resolve()

__starting_point()
