def main():
    n,k = list(map(int,input().split()))
    moves = 2*n
    moves += 1
    moves += min(k-1,n-k)
    moves += n-1

    print (moves)

main()

