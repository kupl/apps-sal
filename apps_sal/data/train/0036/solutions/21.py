from sys import stdin

def main():
    '''
    Name: Kevin S. Sanchez
    Code: B. Worms
    '''
    inp = stdin
    n = int(inp.readline())
    worms = list(map(int, inp.readline().split()))
    J = int(inp.readline())
    Jworms = list(map(int, inp.readline().split()))

    lunch = list()
    
    for i in range (0,len(worms)):
        lunch += [i+1] * worms[i]

    for i in Jworms:
        print(lunch[i-1])

main()

