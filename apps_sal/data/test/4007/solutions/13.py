import sys

n, *f = map(int, sys.stdin.read().split())
f = [None] + f

def main():
    no_receieve = set(range(1, n+1)) - set(f[1:])
    if not no_receieve:
        return f[1:]
    
    no_send = []
    for i in range(1, n+1):
        if f[i] == 0:
            no_send.append(i)
    
    no_send.sort()
    no_receieve = sorted(no_receieve, reverse=True)

    for i in range(len(no_send)):
        if no_send[i] == no_receieve[i]:
            if i >= 1:
                no_send[i], no_send[i-1] = no_send[i-1], no_send[i]
            else:
                no_send[0], no_send[1] = no_send[1], no_send[0]
    
    for i in range(len(no_send)):
        f[no_send[i]] = no_receieve[i]
    
    return f[1:]

def __starting_point():
    ans = main()
    print(*ans, sep=' ')
__starting_point()
