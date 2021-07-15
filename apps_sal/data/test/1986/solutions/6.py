def value(t, f, k):
    if t > k:
        return (f - (t - k))
    else:
        return f


def main():
    first_line = input()
    first_line = first_line.split()
    
    n = int(first_line[0])
    k = int(first_line[1])

    t = []
    f = []
    for i in range(n):
        line = input()
        line = (line.split())
        f += [int(line[0])]
        t += [int(line[1])]

    maximum_index = 0
    maximum = -1 * float("inf")

    for i in range(0, n):
        val = value(t[i], f[i], k)
        if val > maximum:
            maximum = val
            maximum_index = val
            
    print(maximum)
    
        

    

import doctest
doctest.testmod()
main()   

