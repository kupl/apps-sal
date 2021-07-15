def main():
    N = int(input())
    s = list(str(N))
    H = 0
    for i in range(len(s)):
        H += int(s[i])
    if N % H == 0:
        print('Yes')
    else:
        print('No')
    
main()

