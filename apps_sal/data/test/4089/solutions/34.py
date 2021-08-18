N = int(input())
Z = 26
retval = ''
while(N > 0):
    retval = chr((N - 1) % Z + 97) + retval
    N = (N - 1) // Z

print(retval)
