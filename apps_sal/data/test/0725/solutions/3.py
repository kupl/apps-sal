def main():
    n, m = map(int, input().split())
    photo = [input().split() for i in range(n)]
    for i in range(n):
        for j in range(m):
            if photo[i][j] in 'CMY':
                print("#Color")
                return
    print("#Black&White")
        
main()
