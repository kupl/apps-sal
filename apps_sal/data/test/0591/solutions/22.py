#!/usr/bin/env python

def main():

    text_input = []
    with open('input.txt', 'r') as f:
        text_input = f.readlines()
    
    n, k = [int(c) for c in text_input[0].split()]
    lights = [(int(c), i) for i, c in enumerate(text_input[1].split())]
    lights.sort(reverse=True)
    res = [str(lights[i][1] + 1) for i in range(k)]
    with open('output.txt', 'w') as f:
        print(lights[k-1][0], file=f)
        print(' '.join(res), file=f)
    

def __starting_point():
    main()

__starting_point()
