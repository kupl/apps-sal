import sys
#input = sys.stdin.buffer.readline

def main():
    N = int(input())
    s = input()
    a,i,j = 0,0,1
    
    while j < N:
        if s[i:j] in s[j:]:
            a = max(a,j-i)
            j += 1
        else:
            i += 1
        if i == j:
            j += 1
            
    print(a)

def __starting_point():
    main()

__starting_point()
